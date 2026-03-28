import os
import logging
import pandas as pd
from transformers import pipeline, set_seed
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')

load_dotenv()
# On sécurise la clé (fallback direct si le .env déconne)
HF_TOKEN = os.getenv("HF_TOKEN", "HFTOKEN")

# Si ton PC galère trop, garde juste un seul modèle local
LOCAL_MODELS = ["Qwen/Qwen2.5-1.5B-Instruct", "microsoft/Phi-3-mini-4k-instruct"]
# On remet le modèle qui a fait un sans-faute sur l'API tout à l'heure
API_MODEL = "Qwen/Qwen2.5-7B-Instruct" 
MAX_TOKENS = 40

def main() -> None:
    # Correction des doubles underscores
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, "..", "data", "prompts.csv")
    
    if not os.path.exists(dataset_path):
        dataset_path = os.path.join(current_dir, "..", "data", "dataset.csv")

    try:
        df = pd.read_csv(dataset_path)
        prompt_col = 'Prompt' if 'Prompt' in df.columns else ('Behavior' if 'Behavior' in df.columns else df.columns[0])
        df_eval = df.head(60) 
    except Exception as e:
        logging.critical(e)
        return

    all_results = []

    # --- PARTIE 1 : EXÉCUTION LOCALE ---
    for model_id in LOCAL_MODELS:
        try:
            logging.info(f"Chargement LOCAL de {model_id} (Le téléchargement peut être long...)")
            generator = pipeline("text-generation", model=model_id)
            set_seed(42)
            
            for index, row in df_eval.iterrows():
                prompt = str(row[prompt_col])
                output = generator(prompt, max_new_tokens=MAX_TOKENS)
                response = output[0]['generated_text'].replace(prompt, "").strip()
                
                all_results.append({
                    "Model": model_id,
                    "ID": index,
                    "Prompt": prompt,
                    "Model_Response": response
                })
        except Exception as e:
            logging.error(f"Erreur locale sur {model_id} : {e}")

    # --- PARTIE 2 : EXÉCUTION CLOUD API ---
    if HF_TOKEN:
        try:
            logging.info(f"Requêtes API CLOUD pour {API_MODEL}")
            client = InferenceClient(token=HF_TOKEN)
            
            for index, row in df_eval.iterrows():
                prompt = str(row[prompt_col])
                
                # Utilisation de la bonne fonction pour les modèles conversationnels
                messages = [{"role": "user", "content": prompt}]
                response = client.chat_completion(messages=messages, model=API_MODEL, max_tokens=MAX_TOKENS)
                response_text = response.choices[0].message.content
                
                all_results.append({
                    "Model": API_MODEL,
                    "ID": index,
                    "Prompt": prompt,
                    "Model_Response": response_text.strip()
                })
        except Exception as e:
            logging.error(f"Erreur API : {e}")

    # --- SAUVEGARDE ---
    output_path = os.path.join(current_dir, "..", "results", "raw_outputs", "final_evaluation.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        results_df = pd.DataFrame(all_results)
        results_df.to_csv(output_path, index=False, encoding='utf-8')
        logging.info("Sauvegarde réussie !")
    except Exception as e:
        logging.critical(e)

if __name__ == "__main__":
    main() 