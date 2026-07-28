# Few-Shot Prompting Examples

Few-shot prompting provides a few examples of the input/output pattern before asking the model to continue, which helps it understand the exact format expected.

## Example - Converting Log Lines to a Structured Format

```
Prompt:
Convert each log line into JSON with fields: level, service, message.

Log: [ERROR] auth-service - Failed login attempt for user admin
JSON: {"level": "ERROR", "service": "auth-service", "message": "Failed login attempt for user admin"}

Log: [INFO] billing-service - Invoice generated successfully
JSON: {"level": "INFO", "service": "billing-service", "message": "Invoice generated successfully"}

Log: [WARN] api-gateway - Rate limit threshold reached for client 42
JSON:
```

The model is expected to continue the pattern and produce the JSON for the third log line.

## Why Few-Shot Helps

By showing 2 input/output examples first, the model infers the exact schema and formatting to use, reducing ambiguity compared to a zero-shot request.

