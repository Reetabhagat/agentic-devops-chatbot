# ci_fix_agent.py

def ci_fix_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- JENKINS FAILURES ----------
    if "jenkins" in user_input and any(word in user_input for word in ["fail", "failed", "error"]):
        return """
🔴 Jenkins build failed – common reasons:

1. ❌ Wrong credentials (Git / Docker / AWS)
2. ❌ Agent node down or offline
3. ❌ Jenkinsfile syntax error
4. ❌ Missing tools (docker, maven, node, java)
5. ❌ Permission denied on workspace
6. ❌ Disk full on Jenkins node

✅ Fix steps:
- Check Console Output
- Validate Jenkinsfile syntax
- Verify credentials bindings
- Ensure agent has required tools
- Check node disk & memory
"""

    # ---------- PIPELINE FAILED ----------
    if "pipeline failed" in user_input or "pipeline fail" in user_input:
        return """
🔴 CI Pipeline failed – debugging checklist:

1. Identify which stage failed
2. Check exact error message
3. Verify environment variables
4. Validate secrets / credentials
5. Check Docker build & push logs

✅ Pro tip:
Re-run pipeline with debug logs enabled.
"""

    # ---------- GITHUB ACTIONS FAIL ----------
    if "github actions" in user_input and any(word in user_input for word in ["fail", "failed", "error"]):
        return """
🔴 GitHub Actions failed – common causes:

1. ❌ YAML indentation issues
2. ❌ Missing permissions
3. ❌ Secrets not configured
4. ❌ Docker login failure
5. ❌ Wrong runner OS

✅ Fix steps:
- Open Actions → Job logs
- Validate workflow YAML
- Add permissions block:

permissions:
  contents: read
  packages: write
"""

    # ---------- PERMISSION DENIED ----------
    if "permission denied" in user_input:
        return """
🔴 Permission denied error – fixes by tool:

🟡 Jenkins:
- chmod +x script.sh
- Fix workspace ownership
- Check agent user permissions
- Verify sudo access

🟢 GitHub Actions:
- Add permissions block
- Use correct GITHUB_TOKEN
- Check repository access
"""

    # ---------- GENERIC CI FAILURE ----------
    if any(word in user_input for word in ["ci", "cd", "build", "deploy"]) and "fail" in user_input:
        return """
🔴 CI/CD failure – general checklist:

1. Check logs first (always)
2. Verify credentials & secrets
3. Check network / proxy issues
4. Validate YAML / Jenkinsfile
5. Ensure tools are installed

Rule:
Logs > Guessing ❌
Logs > Fix ✅
"""

    return "❌ CI Fix Agent could not clearly identify the issue. Please share more details."
