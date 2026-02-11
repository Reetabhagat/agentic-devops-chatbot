# cloudwatch_agent.py

def cloudwatch_agent(user_input: str):
    user_input = user_input.lower()

    if "alarm" in user_input:
        return """
CloudWatch Alarm not firing:

Checklist:
1. Metric correct?
2. Threshold valid?
3. Evaluation periods set?
4. Alarm state OK/ALARM?
"""

    if "logs" in user_input:
        return """
CloudWatch Logs issue:

Fix:
- IAM role has logs:PutLogEvents
- Correct log group
- App writing logs to stdout
"""

    return "CloudWatch Agent: command not recognized."
