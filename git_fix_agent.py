def git_fix_agent(user_input: str):
    user_input = user_input.lower()

    # Untracked files
    if "untracked" in user_input:
        return (
            "Untracked files mean Git has found new files that are not added yet.\n\n"
            "Fix:\n"
            "1. Add all files:\n"
            "   git add .\n"
            "2. Commit:\n"
            "   git commit -m \"Add files\""
        )

    # Nothing to commit
    if "nothing to commit" in user_input:
        return (
            "Nothing to commit means there are no changes staged.\n\n"
            "Fix:\n"
            "- Modify a file OR\n"
            "- Run `git status` to confirm working tree state"
        )

    # Push rejected
    if "push rejected" in user_input or "failed to push" in user_input:
        return (
            "Push rejected usually means remote has new commits.\n\n"
            "Fix:\n"
            "1. git pull --rebase\n"
            "2. Resolve conflicts if any\n"
            "3. git push"
        )

    # Merge conflict
    if "merge conflict" in user_input:
        return (
            "Merge conflict happens when Git cannot auto-merge changes.\n\n"
            "Fix:\n"
            "1. Open conflicted files\n"
            "2. Resolve markers (<<<< >>>>)\n"
            "3. git add <file>\n"
            "4. git commit"
        )

    return "I understand Git basics. Try asking about untracked files, push errors, or merge conflicts."
