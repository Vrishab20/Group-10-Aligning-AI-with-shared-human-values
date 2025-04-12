
# 🏛️ Ethical Reasoning with LLMs: ChatGPT-4o vs Qwen 2.5

This repository benchmarks **two large language models** — **ChatGPT-4o** and **Qwen 2.5-VL-32B** — on the [ETHICS dataset](https://github.com/hendrycks/ethics), a diverse benchmark comprising moral reasoning questions across five categories: **Commonsense**, **Deontology**, **Justice**, **Virtue**, and **Utilitarianism**.

The [original ETHICS paper](https://arxiv.org/pdf/2008.02275v6) was released before modern LLMs became widespread, making it an ideal benchmark to evaluate how today’s models align with human ethical judgments.

###  Objectives

- Evaluate the ethical reasoning of ChatGPT-4o and Qwen 2.5 across four categories: **Commonsense**, **Justice**, **Virtue**, and **Deontology**
- Compare the effect of three prompting strategies: **baseline**, **few-shot**, and **role-based prompting**
- Visualize keyword influence and model behavior across datasets
- Report and compare performance using four evaluation metrics: **Accuracy**, **Precision**, **Recall**, and **F1 Score**

---

### 📁 Repository Structure

| File/Folder | Description |
|-------------|-------------|
| `ChatGPT_4o_Predictions/` | Contains `.csv` files with responses and labels generated from ChatGPT-4o across all four datasets |
| `predictions_qwen/` | Stores `.csv` outputs from Qwen 2.5-VL-32B model via OpenRouter API |
| `ChatGPT_4o_Evaluation.ipynb` | Code notebook to evaluate ChatGPT-4o predictions using performance metrics |
| `Qwen_2_5_Evaluation.ipynb` | Evaluation notebook for Qwen model predictions |
| `Graphs.ipynb` | Visualizes keyword frequency trends across models, with a focus on the Justice dataset |
| `qwen.ipynb` | Core script to run the Qwen model through API-based prompt execution |
| `ChatGPT_4o_Prompt_History.pdf` | A compiled record of prompts and responses from ChatGPT-4o across all tasks |
| `README.md` | Overview of the project, goals, methodology, and instructions |

---

###  Evaluation Metrics

Performance across datasets is measured using:

- **Accuracy** – Overall correctness  
- **Precision** – How accurate the positive predictions were  
- **Recall** – How many true positive cases were identified  
- **F1 Score** – Harmonic mean of precision and recall

---

###  Prompting Strategies

We implemented three prompting formats:

1. **Baseline** – A direct question with no context  
2. **Few-shot** – Includes a few labeled examples before the query  
3. **Role-based** – Frames the model as an expert in the ethical domain


## ⚖️ Benchmark Results

The table below shows model performance across four ethical reasoning datasets and the average score:

| Model                       |   Justice |   Deontology |   Virtue Ethics |   Commonsense |   Average |
|-----------------------------|-----------|--------------|-----------------|---------------|-----------|
| Random Baseline             |       6.3 |          6.3 |             8.2 |          50   |    17.7   |
| Word Averaging              |      10.3 |         18.2 |             8.5 |          62.9 |    24.975 |
| GPT-3 (few-shot)            |      15.2 |         15.9 |            18.2 |          73.3 |    30.65  |
| BERT-base                   |      26   |         38.8 |            33.1 |          86.5 |    46.1   |
| BERT-large                  |      32.7 |         44.2 |            40.6 |          88.5 |    51.5   |
| ChatGPT 4o (Baseline)       |      54   |         52   |            52   |          50   |    52     |
| ChatGPT 4o (Few-Shot)       |      58   |         76   |            46   |          80   |    65     |
| RoBERTa-large               |      56.7 |         60.3 |            53   |          90.4 |    65.1   |
| ChatGPT 4o (Role-Based)     |      56   |         84   |            78   |          54   |    68     |
| ALBERT-xxlarge              |      59.9 |         64.1 |            64.1 |          85.1 |    68.3   |
| Qwen2.5 VL 32B (Role-Based) |      80   |         86   |            86   |          74   |    81.5   |
| Qwen2.5 VL 32B (Few-Shot)   |      80   |         86   |            90   |          72   |    82     |
| Qwen2.5 VL 32B (Baseline)   |      82   |         92   |            88   |          70   |    83     |
