def helm_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- CREATE HELM CHART ----------
    if "create helm chart" in user_input:
        return """
To create a Helm chart:
helm create my-chart

This creates:
my-chart/
 ├── Chart.yaml
 ├── values.yaml
 └── templates/
"""

    # ---------- HELM INSTALL ----------
    if "helm install" in user_input:
        return """
Helm install command:
helm install my-release my-chart

Example:
helm install nginx-release ./nginx-chart
"""

    # ---------- HELM UPGRADE ----------
    if "helm upgrade" in user_input:
        return """
Helm upgrade command:
helm upgrade my-release my-chart

Used when you change values.yaml or templates.
"""

    # ---------- VALUES.YAML ----------
    if "values.yaml" in user_input:
        return """
values.yaml stores configurable values for Helm charts.

Example:
replicaCount: 2
image:
  repository: nginx
  tag: latest
"""

    # ---------- HELM VS KUBECTL ----------
    if "helm vs kubectl" in user_input or "difference" in user_input:
        return """
kubectl:
- Applies raw YAML files
- No versioning

helm:
- Package manager for Kubernetes
- Supports upgrades, rollback, templating
"""

    return "❌ Helm command not recognized."
