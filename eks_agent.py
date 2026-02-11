# eks_agent.py

def eks_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- CREATE EKS CLUSTER ----------
    if "create eks" in user_input or "create eks cluster" in user_input:
        return """
✅ Steps to create EKS cluster (AWS CLI):

1. Create IAM role for EKS
2. Create EKS cluster:
   aws eks create-cluster \\
     --name demo-cluster \\
     --region us-east-1 \\
     --role-arn <EKS_ROLE_ARN> \\
     --resources-vpc-config subnetIds=subnet-1,subnet-2

3. Create node group:
   aws eks create-nodegroup \\
     --cluster-name demo-cluster \\
     --nodegroup-name demo-nodes \\
     --node-role <NODE_ROLE_ARN> \\
     --subnets subnet-1 subnet-2
"""

    # ---------- UPDATE KUBECONFIG ----------
    if "update kubeconfig" in user_input or "kubectl connect eks" in user_input:
        return """
✅ Update kubeconfig for EKS:

aws eks update-kubeconfig \\
  --region us-east-1 \\
  --name demo-cluster

Then verify:
kubectl get nodes
"""

    # ---------- GET EKS INFO ----------
    if "eks info" in user_input or "describe eks" in user_input:
        return """
📌 Get EKS cluster details:

aws eks describe-cluster \\
  --name demo-cluster \\
  --region us-east-1
"""

    # ---------- EKS ARCHITECTURE ----------
    if "eks architecture" in user_input:
        return """
📘 EKS Architecture:

- Control plane managed by AWS
- Worker nodes in customer VPC
- IAM used for authentication
- kubeconfig used for access
- Nodes communicate via ENI

Key components:
- API Server
- etcd
- Scheduler
- Controller Manager
"""

    return "❌ EKS Agent: I can help with EKS creation, kubeconfig, and architecture."
