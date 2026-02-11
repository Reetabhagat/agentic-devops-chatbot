# docker_agent.py
import subprocess


def docker_agent(user_input: str):
    user_input = user_input.lower()

    try:
        # ---------- DOCKER VERSION ----------
        if "docker version" in user_input:
            result = subprocess.check_output(
                "docker --version", shell=True, text=True
            )
            return result.strip()

        # ---------- DOCKER PS ----------
        if "docker ps" in user_input or "running containers" in user_input:
            result = subprocess.check_output(
                "docker ps", shell=True, text=True
            )
            return result if result else "No running containers"

        # ---------- DOCKER ALL CONTAINERS ----------
        if "all containers" in user_input:
            result = subprocess.check_output(
                "docker ps -a", shell=True, text=True
            )
            return result

        # ---------- DOCKER IMAGES ----------
        if "docker images" in user_input or "list images" in user_input:
            result = subprocess.check_output(
                "docker images", shell=True, text=True
            )
            return result

        # ---------- DOCKER INFO ----------
        if "docker info" in user_input:
            result = subprocess.check_output(
                "docker info", shell=True, text=True
            )
            return result

        return "❌ Docker Agent could not understand the command."

    except subprocess.CalledProcessError as e:
        return f"❌ Docker command failed:\n{e}"
