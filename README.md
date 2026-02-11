# 🤖 Agentic DevOps Chatbot

An AI-powered DevOps Assistant that thinks like a Senior Cloud Engineer.

This project simulates a real-world DevOps support system capable of answering and troubleshooting issues related to:

- AWS
- Terraform
- CI/CD
- Jenkins
- Git & GitHub
- Docker
- Kubernetes
- Linux
- Monitoring (Prometheus, Grafana)

---

## 🧠 Project Overview

Agentic DevOps Chatbot is a modular, domain-based DevOps assistant built using Python and Streamlit.

Each technology has its own agent module:
- aws_agent.py
- terraform_agent.py
- git_agent.py
- kubernetes_agent.py
- linux_agent.py
- monitoring_agent.py
- and more...

A central router directs queries to the correct agent.

---

## 🏗️ Architecture

User → Streamlit UI → Domain Router → Specific Agent → Response

Modular structure allows easy scaling and feature addition.

---

## 🎯 Features

✔ Multi-domain DevOps support  
✔ Modular agent-based design  
✔ Interactive Streamlit UI  
✔ Domain suggestion buttons  
✔ Troubleshooting guidance  
✔ Real-world DevOps use cases  
✔ AWS + Terraform automation examples  

---

## 🖥️ Tech Stack

- Python
- Streamlit
- Git
- AWS
- Terraform
- Docker
- Kubernetes

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/agentic-devops-chatbot.git
cd agentic-devops-chatbot
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
streamlit run app.py


Open in browser:

http://localhost:8501

☁️ Deployment Plan

This project can be deployed on:

AWS EC2

Docker container

Kubernetes cluster

📌 Sample Use Cases

Fix Jenkins build failure

Create Terraform EC2

Debug Git merge conflicts

Solve Docker permission issues

Create EKS cluster

Fix Grafana dashboard issues

🔮 Future Enhancements

Add LLM integration

Intent-based routing

Deployment on AWS EC2

Authentication layer

Persistent chat history

Real AWS SDK integration

👩‍💻 Author

Built by a DevOps AWS Engineer with 3+ years of experience
Focused on Cloud, CI/CD, Automation & Infrastructure as Code.

⭐ Why This Project?

This project demonstrates:

Strong DevOps fundamentals

Infrastructure knowledge

Troubleshooting ability

Modular architecture design

Real-world problem solving
