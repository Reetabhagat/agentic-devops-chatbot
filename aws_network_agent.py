# aws_network_agent.py

def aws_network_agent(user_input: str):
    user_input = user_input.lower()

    if "create vpc" in user_input:
        return """
Example Terraform VPC:

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "main-vpc"
  }
}
"""

    if "public subnet" in user_input:
        return """
Public Subnet:
- Has route to Internet Gateway
- Used for ALB, Bastion, NAT Gateway
"""

    if "private subnet" in user_input:
        return """
Private Subnet:
- No direct internet access
- Used for EC2, EKS worker nodes, databases
"""

    if "internet gateway" in user_input:
        return """
Internet Gateway:
- Allows public subnet resources to access internet
- Must be attached to VPC
"""

    if "route table" in user_input:
        return """
Route Table Issue Checklist:
- Correct subnet association
- 0.0.0.0/0 route present
- IGW or NAT Gateway attached
"""

    return "AWS Network Agent: command not recognized."
