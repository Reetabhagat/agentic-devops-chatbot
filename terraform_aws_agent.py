# terraform_aws_agent.py

def terraform_aws_agent(user_input: str):
    user_input = user_input.lower()

    if "provider" in user_input and "aws" in user_input:
        return """
AWS Provider error in Terraform:

Example provider:
provider "aws" {
  region = "us-east-1"
}

Fix:
- aws configure
- Check IAM permissions
"""

    if "access denied" in user_input:
        return """
Terraform AWS Access Denied:

Reasons:
- IAM user missing permissions
- Wrong AWS profile

Fix:
- Attach required IAM policies
- Export correct AWS_PROFILE
"""

    return "❌ Terraform AWS Agent: no matching case."
