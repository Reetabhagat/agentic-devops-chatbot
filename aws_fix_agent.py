# aws_fix_agent.py

def aws_fix_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- ACCESS DENIED ----------
    if "access denied" in user_input:
        return """
AWS Access Denied – reasons:

1. Missing IAM permissions
2. Wrong role attached
3. Policy not propagated
4. SCP blocking access

Fix:
- Attach correct policy
- Re-login / refresh credentials
"""

    # ---------- EC2 ISSUES ----------
    if "ec2" in user_input and "fail" in user_input:
        return """
EC2 failure reasons:

1. Instance failed status check
2. Disk full
3. Wrong AMI
4. Wrong security group

Fix:
- Check system log
- Reboot instance
- Verify SG & subnet
"""

    # ---------- ALB ISSUES ----------
    if "alb" in user_input and "not working" in user_input:
        return """
ALB not working:

1. Target group unhealthy
2. Wrong health check path
3. SG not allowing traffic
4. App not listening on port

Fix:
- Check target health
- Verify app port
"""

    return "❌ AWS Fix Agent could not identify issue."
