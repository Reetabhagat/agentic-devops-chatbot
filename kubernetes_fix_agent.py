# kubernetes_fix_agent.py

def kubernetes_fix_agent(user_input: str):
    user_input = user_input.lower()

    if "unable to connect" in user_input or "i/o timeout" in user_input:
        return """
Kubernetes cannot connect to the cluster.

Possible reasons:
1. Wrong kubectl context (EKS instead of Docker Desktop)
2. Cluster is not running
3. Network / VPN issue

Fix:
- Run: kubectl config get-contexts
- Switch: kubectl config use-context docker-desktop
- Ensure Docker Desktop Kubernetes is enabled
"""

    if "crashloopbackoff" in user_input:
        return """
CrashLoopBackOff means:
- Container is crashing repeatedly.

Common causes:
1. Application error
2. Wrong command / entrypoint
3. Missing environment variables
4. Image issue

Debug steps:
kubectl describe pod <pod-name>
kubectl logs <pod-name>
"""

    if "pod vs deployment" in user_input:
        return """
Pod vs Deployment:

Pod:
- Smallest unit in Kubernetes
- Runs one or more containers
- No auto-restart guarantee

Deployment:
- Manages Pods
- Auto-restart
- Scaling support
- Rolling updates

👉 Always use Deployment in production.
"""

    return "Kubernetes issue not recognized yet."
