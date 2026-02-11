# tools.py

import subprocess
import platform

def run_command(command_windows: str, command_linux: str):
    os_type = platform.system()

    command = command_windows if os_type == "Windows" else command_linux

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    return {
        "os": os_type,
        "command": command,
        "output": result.stdout.strip(),
        "error": result.stderr.strip()
    }

def format_windows_disk_output(raw_output: str):
    """
    Converts WMIC disk output into readable format
    """
    lines = raw_output.splitlines()
    disks = []

    for line in lines:
        parts = line.split()
        if len(parts) == 3 and parts[0] != "Caption":
            drive = parts[0]
            free = int(parts[1])
            size = int(parts[2])

            used = size - free
            used_percent = round((used / size) * 100, 2)

            disks.append({
                "drive": drive,
                "used_percent": used_percent
            })

    return disks
def format_windows_memory_output(raw_output: str):
    """
    Extracts total physical memory from systeminfo output
    """
    try:
        value = raw_output.split(":")[1].strip()
        return value
    except Exception:
        return "Unknown"


def format_windows_cpu_output(raw_output: str):
    """
    Extracts CPU load percentage
    """
    try:
        return int(raw_output.strip())
    except Exception:
        return None

