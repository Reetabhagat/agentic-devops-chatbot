# github_agent.py

def github_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- CREATE REPO ----------
    if "create" in user_input and "repo" in user_input:
        return (
            "How to create a GitHub repository:\n\n"
            "1. Go to https://github.com\n"
            "2. Click ➕ New repository\n"
            "3. Enter repository name\n"
            "4. Choose public or private\n"
            "5. Click Create repository\n\n"
            "Push local code:\n"
            "git remote add origin <repo-url>\n"
            "git branch -M main\n"
            "git push -u origin main"
        )

    # ---------- PUSH ----------
    if "push" in user_input:
        return (
            "Steps to push code to GitHub:\n\n"
            "git status\n"
            "git add .\n"
            "git commit -m \"commit message\"\n"
            "git push origin main"
        )

    # ---------- PULL ----------
    if "pull" in user_input:
        return (
            "To pull latest changes from GitHub:\n\n"
            "git pull origin main"
        )

    # ---------- PULL REQUEST ----------
    if "pull request" in user_input or "pr" in user_input:
        return (
            "How to create a Pull Request (PR):\n\n"
            "1. Create a new branch\n"
            "2. Push branch to GitHub\n"
            "3. Go to GitHub repo → Pull Requests\n"
            "4. Click New Pull Request\n"
            "5. Select base and compare branch\n"
            "6. Click Create Pull Request"
        )

    # ---------- AUTHENTICATION ----------
    if "authentication" in user_input or "permission denied" in user_input:
        return (
            "GitHub authentication failed because password auth is disabled.\n\n"
            "Fix using Personal Access Token (PAT):\n"
            "1. GitHub → Settings → Developer settings\n"
            "2. Personal access tokens → Generate token\n"
            "3. Use token instead of password"
        )

    # ---------- REPOSITORY NOT FOUND ----------
    if "repository not found" in user_input:
        return (
            "Repository not found error reasons:\n\n"
            "1. Wrong repository URL\n"
            "2. No access to private repo\n"
            "3. Repo does not exist\n\n"
            "Fix:\n"
            "git remote -v\n"
            "Check repo URL and permissions"
        )

    # ---------- FORK ----------
    if "fork" in user_input:
        return (
            "Fork in GitHub:\n\n"
            "A fork is a personal copy of someone else's repository.\n"
            "It allows you to experiment without affecting the original repo."
        )

    return "❌ GitHub Agent could not understand the request."
