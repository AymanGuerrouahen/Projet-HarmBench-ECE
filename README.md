# HarmBench Evaluation: LLM Safety & Ethics Benchmark
**ECE Paris Hackathon - Scientific Project**

## A. Project Presentation
This project evaluates the robustness and ethical alignment of Large Language Models (LLMs) against malicious requests. Using the **HarmBench** methodology, we aim to measure how well different models can withstand adversarial behaviors.

## B. Corpus Description
* **Original Source**: HarmBench Standard Dataset.
* **Experimental Corpus**: A structured sample of 60 prompts categorized by functional risks (e.g., biological/chemical warfare, illegal acts, cybercrime).
* **Methodology**: Automated extraction via local pipeline and Cloud API, followed by qualitative scoring.

## C. Tested Models
We performed a hybrid inference (Local CPU + Hugging Face API) on the following open-source models:
1. **Qwen/Qwen2.5-1.5B-Instruct** (Local Inference)
2. **microsoft/Phi-3-mini-4k-instruct** (Local Inference)
3. **Qwen/Qwen2.5-7B-Instruct** (Cloud API Inference)
* **Parameters**: `max_new_tokens: 40`, `seed: 42` for reproducibility.

## D. Results Summary
| Model | Parameters | Refusal Rate (Safety Score) |
| :--- | :--- | :--- |
| Qwen2.5-1.5B-Instruct | 1.5 Billion | 38.33 % |
| Phi-3-mini-4k-instruct | 3.8 Billion | 33.33 % |
| Qwen2.5-7B-Instruct | 7 Billion | **94.74 %** |

*Conclusion: The results clearly demonstrate the impact of scaling laws on model alignment. The 7B parameter model successfully triggered its guardrails on toxic prompts, whereas smaller edge models (1.5B and 3B) failed to identify the malicious context in over 60% of the cases.*

## E. Project Structure
```text
PROJET-HARMBENCH-ECE-MAIN/
├── analysis/               # Statistical summaries
├── data/                   # Experimental corpus
├── docs/                   # Documentation & Methodology
├── results/raw_outputs/    # Raw model responses (CSV)
├── src/                    # Evaluation (evaluate.py) & execution (main.py) scripts
├── README.md               # Main documentation
└── requirements.txt        # Dependencies