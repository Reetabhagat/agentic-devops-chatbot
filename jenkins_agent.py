# jenkins_agent.py

def jenkins_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- CREATE PIPELINE ----------
    if "create" in user_input and "pipeline" in user_input:
        return """
Here is a basic Jenkins Declarative Pipeline:

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building application'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application'
            }
        }
    }
}
"""

    # ---------- BUILD FAILED ----------
    if "failed" in user_input or "error" in user_input:
        return """
Jenkins build failed. Common reasons:

1. Git checkout failed
2. Missing credentials
3. Docker not installed on agent
4. Permission denied
5. Wrong branch name

Tip:
Check Console Output for exact error.
"""

    # ---------- GENERAL HELP ----------
    return (
        "🤖 Jenkins Agent Help:\n"
        "- create jenkins pipeline\n"
        "- why jenkins build failed\n"
        "- fix jenkins error"
    )
