def grafana_agent(user_input: str):
    user_input = user_input.lower()

    if "install" in user_input or "setup" in user_input:
        return """
📊 Install Grafana using Helm:

1. Add repo:
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update

2. Install:
   helm install grafana grafana/grafana -n monitoring

3. Get admin password:
   kubectl get secret grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 --decode
"""

    if "dashboard not loading" in user_input:
        return """
❌ Grafana dashboard not loading:

Common reasons:
1. Prometheus datasource unreachable
2. Wrong query
3. Time range incorrect
4. Network issue

Fix:
- Settings → Data Sources → Test
- Check Prometheus URL
- Try last 1h time range
"""

    if "login failed" in user_input:
        return """
🔐 Grafana login failed:

Fix:
- Reset admin password
- Check Kubernetes secret
- Restart Grafana pod
"""

    return "❌ Grafana Agent could not understand the query."
