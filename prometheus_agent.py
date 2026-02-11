def prometheus_agent(user_input: str):
    user_input = user_input.lower()

    if "install" in user_input or "setup" in user_input:
        return """
📊 Install Prometheus on Kubernetes:

1. Create namespace:
   kubectl create namespace monitoring

2. Add Helm repo:
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update

3. Install Prometheus:
   helm install prometheus prometheus-community/prometheus -n monitoring
"""

    if "targets down" in user_input:
        return """
❌ Prometheus Targets DOWN:

Common causes:
1. ServiceMonitor misconfigured
2. Wrong labels
3. Pod not reachable
4. NetworkPolicy blocking traffic

Fix:
- kubectl get servicemonitor -n monitoring
- Check target labels
- kubectl describe pod
"""

    if "cpu high" in user_input:
        return """
🔥 Pod CPU HIGH:

Check:
1. kubectl top pod
2. Resource limits set?
3. Infinite loops in app
4. HPA configuration

Fix:
- Add CPU limits
- Scale replicas
- Optimize code
"""

    return "❌ Prometheus Agent could not understand the query."
