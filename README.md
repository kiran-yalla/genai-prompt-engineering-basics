# genai-prompt-engineering-basics

Beginner-friendly examples of core prompt engineering techniques for LLMs: zero-shot, few-shot, chain-of-thought, and role-based prompting.

## What this demonstrates

- 💬 **Core prompting techniques** — zero-shot, few-shot, chain-of-thought, and role-based prompting, each with concrete examples
- 🔌 **Basic API integration** — a simple Python script calling the OpenAI API to run a prompt end-to-end
- 🔐 **Safe credential handling** — the API key is read from an environment variable, never hard-coded

## Structure

```
genai-prompt-engineering-basics/
├── prompts/
│   ├── zero_shot_examples.md         # Direct-ask prompting examples
│   ├── few_shot_examples.md          # Pattern-based prompting examples
│   ├── chain_of_thought_examples.md  # Step-by-step reasoning prompting examples
│   └── role_based_examples.md        # Persona-based prompting examples
├── run_prompt_example.py             # Minimal script to send a prompt to the OpenAI API
└── requirements.txt                  # Python dependencies
```

## Usage

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"
python run_prompt_example.py "Explain what a load balancer does in 2 sentences."
```

> 📘 This is a beginner-level learning repository built while studying prompt engineering fundamentals — not a production prompting framework. See `ai-fundamentals-notes` for related conceptual notes.

## Author

Kiran Yalla — Senior Platform Engineer, DX360°® AI Transformation Certified, currently building foundational skills in generative AI and prompt engineering.
