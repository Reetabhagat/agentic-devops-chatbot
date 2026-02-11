# aws_ecr_agent.py

def aws_ecr_agent(user_input: str):
    user_input = user_input.lower()

    if "create ecr" in user_input:
        return """
Create ECR Repository:

aws ecr create-repository --repository-name my-app

Login to ECR:
aws ecr get-login-password --region us-east-1 \\
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
"""

    if "docker push ecr" in user_input or "push ecr failed" in user_input:
        return """
Docker push to ECR failed – fix:

1. Ensure ECR login done
2. Correct repository URI
3. IAM permission required:
   - AmazonEC2ContainerRegistryFullAccess
"""

    return "AWS ECR Agent: command not recognized."
