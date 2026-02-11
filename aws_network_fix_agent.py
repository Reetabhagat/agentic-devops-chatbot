# aws_network_fix_agent.py

def aws_network_fix_agent(user_input: str):
    user_input = user_input.lower()

    if "ec2 not reachable" in user_input:
        return """
EC2 Not Reachable – Fix Steps:

1. Check Security Group (port 22 / 80 open)
2. Verify subnet is public
3. Internet Gateway attached
4. Route table has 0.0.0.0/0
5. Public IP assigned
"""

    if "nat gateway" in user_input:
        return """
Why NAT Gateway required?

- Private subnet instances need internet access
- Used for updates, Docker pulls, yum/apt
"""

    if "no internet" in user_input:
        return """
No Internet Fix:
- Check IGW
- Check Route Table
- Check NACL
- Check Security Group
"""

    return "AWS Network Fix Agent could not identify the issue."
