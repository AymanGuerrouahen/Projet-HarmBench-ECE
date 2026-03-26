import os
import logging
import pandas as pd
from transformers import pipeline, set_seed

# --- Professional Logging Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Models selected for safety benchmarking
MODELS_TO_TEST = [
    "gpt2",
    "distilgpt2",
    "EleutherAI/gpt-neo-125M"
]
MAX_TOKENS = 40

def main() -> None:
    """
    Executes the HarmBench evaluation pipeline using local CPU inference.
    Ensures data persistence for further analysis in the results directory.
    """
    logging.info("--- Starting Multi-LLM Safety Benchmark ---")

    # 1. Path Resolution and Data Ingestion
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(current_dir, "..", "data", "dataset.csv")

    try:
        df = pd.read_csv(dataset_path)
        # Testing a sample of 10 prompts per model for efficiency
        df_eval = df.head(10) 
        logging.info(f"Dataset successfully loaded: {len(df)} records found.")
    except Exception as e:
        logging.critical(f"Dataset resolution failed: {e}")
        return

    all_results = []

    # 2. Sequential Model Inference Loop
    for model_id in MODELS_TO_TEST:
        logging.info(f"Loading Model: {model_id}...")
        try:
            # Task: 'text-generation' (Standard Causal Language Modeling)
            generator = pipeline("text-generation", model=model_id)
            set_seed(42) # Ensuring scientific reproducibility
            
            for index, row in df_eval.iterrows():
                prompt = str(row.get('Behavior', ''))
                logging.info(f"[{model_id}] Processing prompt {index+1}/10")
                
                # Local inference execution
                output = generator(prompt, max_new_tokens=MAX_TOKENS, pad_token_id=50256)
                response = output[0]['generated_text'].replace(prompt, "").strip()
                
                all_results.append({
                    "Model": model_id,
                    "ID": index,
                    "Prompt": prompt,
                    "Model_Response": response
                })
        except Exception as e:
            logging.error(f"Inference failed for {model_id}: {e}")

    # 3. Data Serialization [cite: 109, 178]
    output_path = os.path.join(current_dir, "..", "results", "raw_outputs", "final_evaluation.csv")
    
    try:
        results_df = pd.DataFrame(all_results)
        results_df.to_csv(output_path, index=False, encoding='utf-8')
        logging.info(f"SUCCESS: Results for all models exported to {output_path}")
    except Exception as e:
        logging.critical(f"I/O Error during file export: {e}")

if __name__ == "__main__":
    main()