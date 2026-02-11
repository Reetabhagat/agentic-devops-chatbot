# ci_agent.py

from jenkins_agent import jenkins_agent
from github_actions_agent import github_actions_agent
from ci_fix_agent import ci_fix_agent


def ci_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- FIX / WHY ----------
    if any(word in user_input for word in ["why", "fail", "error", "fix"]):
        return ci_fix_agent(user_input)

    # ---------- JENKINS ----------
    if "jenkins" in user_input or "pipeline" in user_input:
        return jenkins_agent(user_input)

    # ---------- GITHUB ACTIONS ----------
    if "github actions" in user_input or "workflow" in user_input:
        return github_actions_agent(user_input)

    return "❌ CI agent supports Jenkins & GitHub Actions only."
