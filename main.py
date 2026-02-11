# main.py

from linux_agent import linux_agent
from knowledge import get_basic_answer

from git_agent import git_agent
from git_fix_agent import git_fix_agent
from docker_agent import docker_agent
from docker_fix_agent import docker_fix_agent

from kubernetes_agent import kubernetes_agent
from kubernetes_fix_agent import kubernetes_fix_agent
from kubernetes_yaml_agent import kubernetes_yaml_agent

from helm_agent import helm_agent
from helm_fix_agent import helm_fix_agent

from ci_fix_agent import ci_fix_agent

from aws_network_agent import aws_network_agent
from aws_network_fix_agent import aws_network_fix_agent
from aws_iam_agent import aws_iam_agent
from aws_iam_fix_agent import aws_iam_fix_agent
from aws_auth_agent import aws_auth_agent

from aws_ecr_agent import aws_ecr_agent
from aws_lb_agent import aws_lb_agent
from eks_ingress_agent import eks_ingress_agent
from eks_agent import eks_agent
from eks_fix_agent import eks_fix_agent

from aws_security_agent import aws_security_agent
from cloudwatch_agent import cloudwatch_agent
from aws_cost_agent import aws_cost_agent

from prometheus_agent import prometheus_agent
from grafana_agent import grafana_agent
from monitoring_fix_agent import monitoring_fix_agent

from terraform_agent import terraform_agent


def controller_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- AWS SECURITY ----------
    if any(word in user_input for word in ["kms", "secrets", "parameter store"]):
        return aws_security_agent(user_input)

    # ---------- CLOUDWATCH ----------
    if any(word in user_input for word in ["cloudwatch", "alarm", "logs"]):
        return cloudwatch_agent(user_input)

    # ---------- AWS COST ----------
    if any(word in user_input for word in ["cost", "billing", "budget"]):
        return aws_cost_agent(user_input)

    # ---------- AWS IAM ----------
    if any(word in user_input for word in ["access denied", "assume role", "sts"]):
        return aws_iam_fix_agent(user_input)
    if "iam" in user_input or "role" in user_input:
        return aws_iam_agent(user_input)

    # ---------- AWS NETWORK ----------
    if any(word in user_input for word in ["vpc", "subnet", "nat", "route table", "internet gateway"]):
        return aws_network_agent(user_input)

    # ---------- AWS CONTAINERS ----------
    if "ecr" in user_input:
        return aws_ecr_agent(user_input)
    if "alb" in user_input or "load balancer" in user_input:
        return aws_lb_agent(user_input)
    if "ingress" in user_input:
        return eks_ingress_agent(user_input)
    if "eks" in user_input:
        return eks_agent(user_input)

    # ---------- CI/CD ----------
    if any(word in user_input for word in ["jenkins", "pipeline", "github actions", "ci", "cd"]):
        return ci_fix_agent(user_input)

    # ---------- TERRAFORM ----------
    if "terraform" in user_input:
        return terraform_agent(user_input)

    # ---------- K8S / DOCKER / GIT ----------
    if "kubectl" in user_input or "kubernetes" in user_input:
        return kubernetes_agent(user_input)
    if "docker" in user_input:
        return docker_agent(user_input)
    if "git" in user_input:
        return git_agent(user_input)

    basic = get_basic_answer(user_input)
    if basic:
        return basic

    return "❌ I support DevOps, AWS, CI/CD, Containers, Monitoring & Terraform queries only."


if __name__ == "__main__":
    while True:
        user_input = input("\n🧑‍💻 Ask DevOps Agent (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("👋 Exiting DevOps Agent")
            break

        print(controller_agent(user_input))
