# Chain-of-Thought Prompting Examples

Chain-of-thought (CoT) prompting asks the model to reason step-by-step before giving a final answer, which tends to improve accuracy on multi-step problems.

## Example - Basic Reasoning

```
Prompt: A server handles 120 requests per minute. If traffic increases by 25%,
how many requests per minute will it handle? Think step by step, then give the final answer.
```

Expected reasoning pattern:

```
Step 1: Current rate = 120 requests/minute
Step 2: Increase = 25% of 120 = 30
Step 3: New rate = 120 + 30 = 150
Final answer: 150 requests per minute
```

## Example - Troubleshooting Style

```
Prompt: A web app returns HTTP 502 errors intermittently. Walk through the most likely
causes step by step, from most to least common, before suggesting next troubleshooting steps.
```

## Why This Helps

Explicitly asking for step-by-step reasoning reduces the chance the model jumps to an incorrect conclusion, especially for arithmetic, logic, or multi-step diagnostic tasks.

