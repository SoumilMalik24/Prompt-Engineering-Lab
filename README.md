<h1 align="center">
Prompt Engineering Lab
<h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Prompt_Engineering-Core%20to%20Advanced-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLMs-OpenAI%20%7C%20Anthropic%20%7C%20OpenSource-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Reasoning%20%7C%20Formatting%20%7C%20Control-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" />
</p>

---

## Overview

**Prompt Engineering Lab** is a **hands-on, experiment-driven repository** that demonstrates **how different prompt design strategies affect Large Language Model (LLM) behavior**.

Instead of theory-heavy explanations, this lab focuses on:

* Practical prompt patterns
* Model controllability
* Reasoning improvements
* Output structure enforcement
* Open-source LLM compatibility

This repository is designed to be:

* A **learning reference**
* A **prompt experimentation sandbox**
* A **foundation for RAG / Agentic AI systems**
* A **strong portfolio project**

---

## What You Will Learn

* How models behave under **zero-shot, one-shot, and few-shot** settings
* How **Chain-of-Thought** improves reasoning reliability
* How to **control output formats** (JSON, schemas, templates)
* How different **prompt schemas** work across models
* How instruction formatting affects **open-source LLMs**

---

## Repository Structure & Contents

This lab is organized by **prompting strategy**, not by provider.

| File                       | Purpose                                                              |
| -------------------------- | -------------------------------------------------------------------- |
| **`Zero-Shot.py`**         | Task execution without examples; relies purely on model pretraining. |
| **`One-Shot.py`**          | Uses a single example to guide response style and accuracy.          |
| **`Few-Shot.py`**          | Multiple demonstrations to improve consistency and reduce ambiguity. |
| **`Chain-Of-Thought.py`**  | Explicit step-by-step reasoning for logic and math tasks.            |
| **`Auto_COT.py`**          | Automatically generates reasoning steps instead of hardcoding them.  |
| **`Persona_Prompt.py`**    | Assigns expert roles or personalities to shape responses.            |
| **`Structured-Output.py`** | Forces strict output formats like JSON or schema-based responses.    |
| **`Alpaca-Prompt.py`**     | Instruction tuning format used in Alpaca-style datasets.             |
| **`ChatML-Schema.py`**     | ChatML formatting for chat-based LLMs.                               |
| **`INST-Format.py`**       | `[INST] ... [/INST]` format used by LLaMA / Mistral models.          |

---

## Prompting Techniques Covered

<p align="left">
  <img src="https://img.shields.io/badge/Zero--Shot-Basics-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Few--Shot-Accuracy-success?style=flat-square" />
  <img src="https://img.shields.io/badge/Chain_of_Thought-Reasoning-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Persona-Prompting-black?style=flat-square" />
  <img src="https://img.shields.io/badge/Structured_Output-JSON%20%7C%20Schemas-purple?style=flat-square" />
</p>

---

## Getting Started

### Prerequisites

* Python **3.8 or higher**
* One of the following:

  * OpenAI API key
  * Anthropic API key
  * Local / open-source LLM setup

---

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/SoumilMalik24/Prompt-Engineering-Lab.git
cd Prompt-Engineering-Lab
```

#### 2. (Optional but recommended) Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # Linux / Mac
```

#### 3. Install dependencies

```bash
pip install openai python-dotenv
```

> Individual scripts may require additional libraries depending on the provider.

---

## Environment Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

> Never commit `.env` files to version control.

---

## Usage

Run any experiment directly as a Python script.

```bash
# Example: Chain of Thought prompting
python Chain-Of-Thought.py
```

Each file is **self-contained** and focuses on **one prompting concept at a time**.

---

## Concepts Explained (Brief)

### Zero-Shot vs Few-Shot

* **Zero-shot**: Fast, general-purpose, but less precise
* **Few-shot**: Higher accuracy, better formatting, more control

### Chain of Thought (CoT)

Encourages models to reason step-by-step instead of jumping to answers, improving:

* Logical reasoning
* Math accuracy
* Explainability

### Prompt Schemas (Alpaca, ChatML, INST)

Open-source models depend heavily on **exact prompt formatting**.
Incorrect schemas can lead to:

* Truncated outputs
* Ignored instructions
* Role confusion

This lab provides **ready-to-use templates**.

---

## Who Is This For?

* Students learning **Generative AI**
* Engineers working with **LLMs & RAG**
* Researchers testing **prompt sensitivity**
* Developers using **open-source LLMs**
* Anyone serious about **LLM controllability**

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Add your prompting technique or improvement
4. Open a Pull Request

Well-documented and clean examples are preferred.

---

## License

This project is released under the **MIT License**.

