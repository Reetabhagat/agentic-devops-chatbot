import subprocess

def run_kubectl(command):
    try:
        result = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        return f"❌ Kubernetes command failed:\n{e.output}"


def kubernetes_agent(user_input: str):
    user_input = user_input.lower()

    if "kubectl version" in user_input or "kubernetes version" in user_input:
        return run_kubectl("kubectl version --client")

    if "get nodes" in user_input:
        return run_kubectl("kubectl get nodes")

    if "get pods" in user_input:
        return run_kubectl("kubectl get pods")

    if "all pods" in user_input:
        return run_kubectl("kubectl get pods -A")

    if "describe pod" in user_input:
        return "ℹ️ Usage: describe pod <pod-name>\nExample:\n kubectl describe pod nginx-pod"

    if "crashloopbackoff" in user_input:
        return """
❌ CrashLoopBackOff means container is crashing repeatedly.

✅ Common fixes:
1. Check logs:
   kubectl logs <pod-name>
2. Describe pod:
   kubectl describe pod <pod-name>
3. Fix app config / env vars
"""

    if "imagepullbackoff" in user_input:
        return """
❌ ImagePullBackOff means Kubernetes cannot pull image.

✅ Fix:
1. Check image name
2. Check DockerHub credentials
3. Try:
   kubectl describe pod <pod-name>
"""

    return "❌ Kubernetes command not supported yet."
