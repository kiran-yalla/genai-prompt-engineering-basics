"""
run_prompt_example.py

A simple, beginner-level script demonstrating how to send a prompt to an LLM
using the OpenAI API. Reads the API key from an environment variable so no
secrets are ever hard-coded in the script.

Usage:
    export OPENAI_API_KEY="your-key-here"
    python run_prompt_example.py "Explain what a load balancer does in 2 sentences."
"""

import os
import sys

from openai import OpenAI


def run_prompt(prompt_text: str, model: str = "gpt-4o-mini") -> str:
    """Send a single prompt to the model and return the text response."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY environment variable not set. "
            "Set it before running this script."
        )

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful, concise assistant."},
            {"role": "user", "content": prompt_text},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_prompt_example.py \"<your prompt here>\"")
        sys.exit(1)

    prompt_text = " ".join(sys.argv[1:])
    print(f"Prompt: {prompt_text}\n")

    answer = run_prompt(prompt_text)
    print("Response:")
    print(answer)


if __name__ == "__main__":
    main()

