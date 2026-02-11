# aws_lb_agent.py

def aws_lb_agent(user_input: str):
    user_input = user_input.lower()

    if "create alb" in user_input or "application load balancer" in user_input:
        return """
Create ALB steps:

1. EC2 → Load Balancers → Create
2. Application Load Balancer
3. Select VPC + subnets
4. Create Target Group
5. Register EC2 / Pods
"""

    if "target unhealthy" in user_input:
        return """
ALB Target Unhealthy – reasons:

1. Wrong health check path
2. App not listening on port
3. Security Group blocked
4. Pod crashed

Fix:
- Verify health check
- Check app logs
"""

    return "AWS Load Balancer Agent: command not recognized."
