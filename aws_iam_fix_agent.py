# aws_iam_fix_agent.py

def aws_iam_fix_agent(user_input: str):
    user_input = user_input.lower()

    if "access denied" in user_input:
        return """
AWS AccessDenied error – common causes:

1. Missing IAM policy
2. Wrong role assumed
3. SCP blocking access
4. Policy not propagated yet

Fix:
- Attach correct policy
- Re-login / refresh creds
"""

    if "assume role" in user_input or "sts" in user_input:
        return """
STS AssumeRole failed:

Checklist:
- Trust policy allows principal
- Correct role ARN
- sts:AssumeRole permission present

Test:
aws sts get-caller-identity
"""

    if "github actions" in user_input and "aws" in user_input:
        return """
GitHub Actions → AWS Auth (OIDC):

Steps:
1. Create IAM OIDC provider
2. Create role with trust policy
3. Use aws-actions/configure-aws-credentials

No access keys needed.
"""

    return "AWS IAM Fix Agent could not identify issue."
