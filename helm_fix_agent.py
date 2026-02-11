def helm_fix_agent(user_input: str):
    user_input = user_input.lower()

    if "failed" in user_input or "error" in user_input:
        return """
Common Helm errors & fixes:

1. Release already exists
Fix:
helm upgrade <release> <chart>

2. Values.yaml syntax error
Fix:
Check indentation and spacing

3. Chart not found
Fix:
Run helm repo update
"""

    return ""
