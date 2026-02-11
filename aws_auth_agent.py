# aws_auth_agent.py

def aws_auth_agent(user_input: str):
    user_input = user_input.lower()

    if "aws configure" in user_input or "cli not configured" in user_input:
        return """
AWS CLI not configured:

Run:
aws configure

Check:
aws sts get-caller-identity
"""

    if "profile" in user_input:
        return """
AWS Profile Issue:

List profiles:
aws configure list-profiles

Set profile:
export AWS_PROFILE=dev   (Linux)
set AWS_PROFILE=dev      (Windows)
"""

    if "token expired" in user_input:
        return """
AWS Token Expired:

Fix:
- Re-login (SSO)
- Re-run aws configure
- Refresh credentials
"""

    return "AWS Auth Agent: auth issue not recognized."
