# eks_ingress_agent.py

def eks_ingress_agent(user_input: str):
    user_input = user_input.lower()

    if "ingress" in user_input and "eks" in user_input:
        return """
EKS Ingress with ALB (AWS Load Balancer Controller):

Steps:
1. Install AWS Load Balancer Controller
2. Create Ingress YAML
3. Annotate ingress with alb

Ingress annotation example:
alb.ingress.kubernetes.io/scheme: internet-facing
"""

    if "ingress not working" in user_input:
        return """
Ingress not working – checklist:

1. Controller installed?
2. Correct annotations?
3. Service type correct?
4. IAM role attached?

Check:
kubectl get ingress
kubectl logs controller-pod
"""

    return "EKS Ingress Agent: command not recognized."
