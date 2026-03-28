# HarmBench Evaluation: LLM Safety & Ethics Benchmark
**ECE Paris Hackathon - Scientific Project**

## A. Project Presentation
[cite_start]This project evaluates the robustness and ethical alignment of Large Language Models (LLMs) against malicious requests[cite: 118, 119]. [cite_start]Using the **HarmBench** methodology, we aim to measure how well different models can withstand adversarial behaviors[cite: 120, 121].

## B. Corpus Description
* [cite_start]**Original Source**: HarmBench Standard Dataset[cite: 123].
* [cite_start]**Experimental Corpus**: A structured sample of 400 prompts categorized by functional risks (e.g., biological/chemical warfare, illegal acts)[cite: 124, 126].
* [cite_start]**Methodology**: Automated extraction and qualitative scoring[cite: 125].

## C. Tested Models
[cite_start]We performed local CPU inference on the following open-source models[cite: 127, 128]:
1. [cite_start]**GPT-2** (Base Causal Model) [cite: 129]
2. [cite_start]**DistilGPT2** (Compressed version) [cite: 129]
3. [cite_start]**GPT-Neo-125M** (EleutherAI) [cite: 129]
* [cite_start]**Parameters**: `max_new_tokens: 40`, `seed: 42` for reproducibility[cite: 131].

## D. Results Summary
| Model | Refusal Rate (Safety Score) |
| :--- | :--- |
| GPT-2 | 0.00 % |
| DistilGPT2 | 0.00 % |
| GPT-Neo-125M | 10.00 % |

## E. Project Structure
```text
PROJET-HARMBENCH-ECE-MAIN/
├── analysis/               # Statistical summaries [cite: 153]
├── data/                   # Experimental corpus [cite: 142]
├── docs/                   # Documentation & Methodology [cite: 155]
├── results/raw_outputs/    # Raw model responses [cite: 149, 150]
├── src/                    # Evaluation & execution scripts [cite: 145]
├── README.md               # Main documentation [cite: 140]
└── requirements.txt        # Dependencies [cite: 141]