# Project: Evaluating LLM Robustness with HarmBench

## Description
[cite_start]This project aims to evaluate the safety and ethics of Large Language Models (LLMs) against malicious requests[cite: 85]. [cite_start]We rely on the **HarmBench** methodology to measure the models' ability to withstand attacks[cite: 90].

## Objectives
1. [cite_start]Analyze security vulnerabilities in current models (open and proprietary)[cite: 100].
2. [cite_start]Compare the results obtained with other benchmarks[cite: 98].
3. [cite_start]Propose an analysis grid for responses (refusal rate, justification, harmfulness)[cite: 101].

## Methodology
[cite_start]We test the models on three main axes[cite: 102]:
* [cite_start]**Harmbench_contextual**: Prompt injections designed to deceive the context[cite: 103].
* [cite_start]**Harmbench_copyright**: Requests for copyright-protected information[cite: 105].
* [cite_start]**Harmbench_standard**: Classic dangerous behaviors and harm to others[cite: 106].

## Project Structure
* `/data`: Contains prompt datasets (trick questions).
* `/src`: Contains the Python evaluation scripts.
* `/docs`: Contains the final report and analyses.
