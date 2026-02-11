# aws_agent.py

def aws_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- EC2 ----------
    if "create ec2" in user_input:
        return """
Create EC2 Instance (AWS Console):

1. Go to EC2 → Launch Instance
2. Choose AMI (Amazon Linux 2)
3. Instance type (t2.micro)
4. Configure key pair
5. Open port 22 / 80 in Security Group
6. Launch instance
"""

    if "ec2 not reachable" in user_input:
        return """
EC2 not reachable – checklist:

1. Security Group allows inbound traffic
2. Correct key pair used
3. Instance is running
4. Public IP assigned
5. NACL not blocking traffic
"""

    # ---------- IAM ----------
    if "iam" in user_input:
        return """
IAM basics:

IAM components:
- Users
- Groups
- Roles
- Policies

Best practice:
- Use roles, not access keys
- Least privilege policy
"""

    # ---------- ALB ----------
    if "load balancer" in user_input or "alb" in user_input:
        return """
Create ALB:

1. EC2 → Load Balancers → Create
2. Application Load Balancer
3. Select VPC + subnets
4. Configure listener (80/443)
5. Attach Target Group
"""

    # ---------- ASG ----------
    if "autoscaling" in user_input:
        return """
Auto Scaling Group flow:

1. Create Launch Template
2. Create ASG
3. Attach Load Balancer
4. Configure scaling policy
"""

    # ---------- EKS HIGH LEVEL ----------
    if "eks" in user_input:
        return """
EKS Architecture:

- Control plane (managed by AWS)
- Worker nodes (EC2)
- IAM + VPC + Security Groups
- kubectl talks to API Server
"""

    return "❌ AWS Agent: command not recognized."
