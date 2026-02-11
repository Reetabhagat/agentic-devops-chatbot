# terraform_agent.py

def terraform_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- BASIC COMMANDS ----------
    if "terraform init" in user_input:
        return """
terraform init initializes Terraform directory.

Common options:
terraform init -upgrade
terraform init -reconfigure
"""

    if "terraform plan" in user_input:
        return """
terraform plan shows infra changes.

terraform plan -out=tfplan
"""

    if "terraform apply" in user_input:
        return """
terraform apply creates infrastructure.

terraform apply tfplan
"""

    if "terraform destroy" in user_input:
        return """
terraform destroy deletes all infra.

⚠️ Avoid running in production
"""

    # ---------- EC2 ----------
    if "terraform ec2" in user_input or "create terraform ec2" in user_input:
        return """
Terraform EC2 example:

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "demo" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  tags = {
    Name = "terraform-ec2"
  }
}
"""

    # ---------- S3 ----------
    if "terraform s3" in user_input or "create terraform s3" in user_input:
        return """
Terraform S3 bucket:

resource "aws_s3_bucket" "demo" {
  bucket = "my-terraform-bucket-123"
}

Best practice:
- Enable versioning
- Enable encryption
"""

    # ---------- VPC ----------
    if "terraform vpc" in user_input:
        return """
Terraform VPC:

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "main-vpc"
  }
}
"""

    # ---------- IAM ----------
    if "terraform iam" in user_input or "iam role" in user_input:
        return """
Terraform IAM Role:

resource "aws_iam_role" "ec2_role" {
  name = "ec2-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}
"""

    # ---------- BACKEND ----------
    if "terraform backend" in user_input or "remote state" in user_input:
        return """
Terraform remote backend (S3):

terraform {
  backend "s3" {
    bucket = "tf-state-bucket"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "tf-lock"
  }
}
"""

    # ---------- MODULES ----------
    if "terraform module" in user_input:
        return """
Terraform module usage:

module "ec2" {
  source = "./modules/ec2"
  instance_type = "t2.micro"
}
"""

    # ---------- BEST PRACTICES ----------
    if "terraform best practice" in user_input:
        return """
Terraform Best Practices:

1. Use remote backend
2. Use modules
3. Separate env (dev/stage/prod)
4. Never hardcode secrets
5. Use terraform validate
6. Use state locking
"""

    return "❌ Terraform Agent: command not recognized."
