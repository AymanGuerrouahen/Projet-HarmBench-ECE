import os
from huggingface_hub import InferenceClient
import pandas as pd
import time

HF_TOKEN = "hf_...CCQH"
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.2"

def query_ai(question):
    print(f"Sending question: {question[:50]}...")
    client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)
    try:
        response = client.text_generation(question, max_new_tokens=200)
        return response
    except Exception as e:
        return f"Error: {e}"

def main():
    print("--- Starting HarmBench Benchmark ---")

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "../data/prompts.csv")
        
        if not os.path.exists(csv_path):
            csv_path = "data/prompts.csv"
            
        df = pd.read_csv(csv_path)
        print(f"{len(df)} questions loaded.")
    except Exception as e:
        print(f"CRITICAL: Unable to read the file. Check the path! Error: {e}")
        return

    results = []

    for index, row in df.iterrows():
        if 'Prompt_Question' not in row:
            print("ERROR: The column 'Prompt_Question' does not exist in the CSV!")
            break

        prompt = row['Prompt_Question']
        response = query_ai(prompt)

        results.append({
            "ID": row.get('ID', index),
            "Type": row.get('Type_Attaque', 'Unknown'),
            "Question": prompt,
            "Reponse_IA": response
        })

        time.sleep(1)

    df_res = pd.DataFrame(results)
    df_res.to_csv("resultats_final.csv", index=False)
    print("--- Finished! Results saved in 'resultats_final.csv' ---")

if __name__ == "__main__":
    main()
