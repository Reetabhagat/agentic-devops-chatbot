# aws_cost_agent.py

def aws_cost_agent(user_input: str):
    user_input = user_input.lower()

    if "cost high" in user_input or "aws bill" in user_input:
        return """
AWS bill high – top reasons:

1. EC2 running 24x7
2. NAT Gateway charges
3. Unused EBS volumes
4. Data transfer
5. No autoscaling

Fix:
- Stop unused EC2
- Delete unattached EBS
- Use Savings Plans
"""

    if "budget" in user_input:
        return """
Enable AWS Budget:

Steps:
1. AWS Billing → Budgets
2. Create cost budget
3. Set alert threshold
4. Add email/SNS
"""

    if "reduce cost" in user_input:
        return """
Cost Optimization Tips:

- Right-size instances
- Use Spot for non-prod
- S3 lifecycle rules
- Auto Scaling
"""

    return "AWS Cost Agent: command not recognized."
