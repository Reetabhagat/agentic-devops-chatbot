# knowledge.py

BASIC_KNOWLEDGE = {
    "what is devops": "DevOps is a set of practices that combines software development and IT operations to improve collaboration and delivery speed.",
    "what is docker": "Docker is a containerization platform used to package applications and their dependencies into lightweight containers.",
    "what is kubernetes": "Kubernetes is a container orchestration system used to deploy, scale, and manage containerized applications.",
    "what is terraform": "Terraform is an Infrastructure as Code tool used to provision and manage cloud resources."
}

def get_basic_answer(question: str):
    question = question.lower()
    for key in BASIC_KNOWLEDGE:
        if key in question:
            return BASIC_KNOWLEDGE[key]
    return None
