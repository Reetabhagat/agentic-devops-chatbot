# aws_iam_agent.py

def aws_iam_agent(user_input: str):
    user_input = user_input.lower()

    if "iam role vs user" in user_input or "role vs user" in user_input:
        return """
IAM User vs Role:

IAM User:
- Long-term credentials
- For humans

IAM Role:
- Temporary credentials
- For services (EC2, EKS, GitHub Actions)

Best Practice:
Use ROLES, not users.
"""

    if "create iam role" in user_input:
        return """
Create IAM Role (High level):

1. IAM → Roles → Create role
2. Trusted entity (EC2 / EKS / Web Identity)
3. Attach policies
4. Use role in service
"""

    if "least privilege" in user_input:
        return """
Least Privilege Principle:

- Grant minimum required permissions
- Avoid AdministratorAccess
- Scope by resource & action
"""

    if "eks access denied" in user_input:
        return """
EKS Access Denied (IAM side):

- IAM role missing EKS policies
- Not mapped in aws-auth ConfigMap

Policies:
- AmazonEKSClusterPolicy
- AmazonEKSWorkerNodePolicy
"""

    return "AWS IAM Agent: command not recognized."
