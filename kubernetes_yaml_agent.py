# kubernetes_yaml_agent.py

def kubernetes_yaml_agent(user_input: str):
    user_input = user_input.lower()

    # ---------------- DEPLOYMENT ----------------
    if "deployment" in user_input:
        return """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
      - name: demo-container
        image: nginx
        ports:
        - containerPort: 80
"""

    # ---------------- SERVICE ----------------
    if "service" in user_input:
        return """
apiVersion: v1
kind: Service
metadata:
  name: demo-service
spec:
  type: NodePort
  selector:
    app: demo
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
"""

    # ---------------- CONFIGMAP ----------------
    if "configmap" in user_input:
        return """
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo-config
data:
  APP_ENV: production
  APP_DEBUG: "false"
"""

    # ---------------- FULL APP ----------------
    if "full app" in user_input:
        return """
Includes:
✔ Deployment
✔ Service
✔ ConfigMap

Use:
kubectl apply -f <file>.yaml
"""

    return "❌ I can generate Deployment, Service, ConfigMap YAMLs only."
