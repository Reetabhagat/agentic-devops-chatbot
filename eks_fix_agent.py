# eks_fix_agent.py

def eks_fix_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- KUBECTL NOT CONNECTING ----------
    if "kubectl" in user_input and "not" in user_input:
        return """
❌ kubectl not connecting to EKS – common causes:

1. kubeconfig not updated
2. Wrong AWS profile
3. Cluster deleted or region mismatch
4. Security group blocking access
5. IAM role missing permissions

✅ Fix:
aws eks update-kubeconfig --region <region> --name <cluster-name>
"""

    # ---------- NODES NOT JOINING ----------
    if "node" in user_input and "not joining" in user_input:
        return """
❌ EKS nodes not joining cluster:

Common reasons:
1. aws-auth ConfigMap missing node role
2. Worker node IAM role incorrect
3. Security group blocks port 443
4. Wrong AMI or bootstrap failure

Fix:
kubectl edit configmap aws-auth -n kube-system
"""

    # ---------- ACCESS DENIED ----------
    if "access denied" in user_input:
        return """
❌ EKS AccessDenied error:

Reasons:
1. IAM user/role missing eks permissions
2. Not mapped in aws-auth ConfigMap
3. Wrong AWS profile

Fix:
- Attach AmazonEKSClusterPolicy
- Map IAM user in aws-auth
"""

    # ---------- CLUSTER UNREACHABLE ----------
    if "timeout" in user_input or "unable to connect" in user_input:
        return """
❌ Unable to connect to EKS cluster:

Check:
1. Cluster is ACTIVE
2. Correct VPC & subnet
3. Public endpoint enabled
4. Corporate VPN blocking traffic

Run:
aws eks describe-cluster --name <cluster>
"""

    return None
