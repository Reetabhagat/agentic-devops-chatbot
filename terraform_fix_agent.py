# terraform_fix_agent.py

def terraform_fix_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- STATE LOCK ----------
    if "state lock" in user_input or "locked" in user_input:
        return """
Terraform state lock error:

Reason:
- Another terraform process running
- Interrupted apply

Fix:
terraform force-unlock <LOCK_ID>
"""

    # ---------- INIT FAILED ----------
    if "terraform init failed" in user_input or "init error" in user_input:
        return """
Terraform init failed:

Reasons:
1. Provider version mismatch
2. Backend config issue
3. Network issue

Fix:
- terraform init -upgrade
- Check backend block
"""

    # ---------- PLAN ERROR ----------
    if "terraform plan error" in user_input:
        return """
Terraform plan error:

Common causes:
- Missing variables
- Wrong resource arguments
- Invalid provider config

Fix:
- Check variables.tf
- Validate syntax
- terraform validate
"""

    return "❌ Terraform Fix Agent: issue not identified clearly."
