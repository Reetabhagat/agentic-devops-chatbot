def docker_fix_agent(user_input: str):
    user_input = user_input.lower()

    # Docker daemon not running
    if "cannot connect" in user_input or "daemon" in user_input:
        return """
❌ Docker daemon is not running.

✅ Fix:
1. Open Docker Desktop
2. Wait until status shows: "Docker is running"
3. Try again:
   docker ps
"""

    # Docker Desktop not started (Windows)
    if "pipe/dockerdesktoplinuxengine" in user_input:
        return """
❌ Docker Desktop is not running (Windows issue).

✅ Fix:
1. Start Docker Desktop
2. Enable WSL2 backend
3. Restart terminal
"""

    # Port already in use
    if "port" in user_input and "use" in user_input:
        return """
❌ Port already in use.

✅ Fix:
1. Find process using port:
   netstat -ano | findstr :<PORT>
2. Kill process:
   taskkill /PID <PID> /F
OR
3. Use different port:
   docker run -p 8081:80 image_name
"""

    # Image not found
    if "image" in user_input and "not found" in user_input:
        return """
❌ Docker image not found locally.

✅ Fix:
1. Pull image:
   docker pull <image-name>
2. Then run container
"""

    return "❌ Docker issue not recognized yet."
