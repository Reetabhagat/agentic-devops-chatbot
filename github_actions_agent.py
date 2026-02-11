# github_actions_agent.py

def github_actions_agent(user_input: str):
    user_input = user_input.lower()

    # ---------- CREATE WORKFLOW ----------
    if "create" in user_input or "workflow" in user_input:
        return """
GitHub Actions – Docker build workflow example:

name: Docker Build

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t my-app .
"""

    # ---------- DOCKER BUILD ----------
    if "docker" in user_input:
        return """
GitHub Actions – Docker build steps:

- name: Login to DockerHub
  run: docker login -u ${{ secrets.DOCKER_USER }} -p ${{ secrets.DOCKER_PASS }}

- name: Build Image
  run: docker build -t my-app .

- name: Push Image
  run: docker push my-app
"""

    # ---------- PERMISSION ISSUE ----------
    if "permission" in user_input:
        return """
GitHub Actions permission denied fix:

Add this to workflow:

permissions:
  contents: read
  packages: write

Also check:
- Secrets configured
- Correct runner OS
"""

    return "❌ GitHub Actions agent could not understand the request."
