def git_agent(query):
    q = query.lower()

    if "add" in q:
        return """
📌 Git Add

git add is used to move changes to staging area.

Example:
git add file.txt
git add .

Workflow:
Modified file → git add → git commit
"""

    elif "commit" in q:
        return """
📌 Git Commit

git commit -m "your message"

Creates snapshot of staged changes.
"""

    elif "merge" in q:
        return """
📌 Git Merge

git merge branch-name

Used to combine two branches.
"""

    elif "rebase" in q:
        return """
📌 Git Rebase

git rebase branch-name

Rewrites commit history.
Cleaner history than merge.
"""

    elif "conflict" in q:
        return """
⚠️ Merge Conflict Fix

1. Open conflicting file
2. Remove <<<<<<< markers
3. git add .
4. git commit
"""

    elif "reset" in q or "undo" in q:
        return """
📌 Undo Last Commit

Soft reset:
git reset --soft HEAD~1

Hard reset:
git reset --hard HEAD~1
"""

    else:
        return """
🤖 Git Agent Help:

Try asking:
- git add example
- git merge conflict fix
- undo last commit
- git branch strategy
"""
