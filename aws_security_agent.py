# aws_security_agent.py

def aws_security_agent(user_input: str):
    user_input = user_input.lower()

    if "kms" in user_input:
        return """
KMS issues – checklist:
1. Key policy allows your role
2. Correct region
3. Service has kms:Decrypt permission

Fix:
- Update key policy
- Attach kms permissions to role
"""

    if "secrets manager" in user_input:
        return """
Secrets Manager access denied:

Fix:
- Attach SecretsManagerReadWrite policy
- Verify secret ARN
- Check region mismatch
"""

    if "parameter store" in user_input:
        return """
SSM Parameter Store issue:

Fix:
- ssm:GetParameter permission
- Correct parameter path
- Decrypt flag for SecureString
"""

    return "AWS Security Agent: command not recognized."
