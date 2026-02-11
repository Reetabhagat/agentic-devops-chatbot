# linux_agent.py

from tools import (
    run_command,
    format_windows_disk_output,
    format_windows_memory_output,
    format_windows_cpu_output
)

def linux_agent(task: str):
    task = task.lower()

    # ---------- DISK ----------
    if "disk" in task:
        result = run_command(
            command_windows="wmic logicaldisk get size,freespace,caption",
            command_linux="df -h"
        )

        if result["os"] == "Windows":
            disks = format_windows_disk_output(result["output"])
            messages = []

            for d in disks:
                msg = f"Drive {d['drive']} is {d['used_percent']}% used"
                if d["used_percent"] > 80:
                    msg += " ⚠️ HIGH USAGE"
                messages.append(msg)

            return "\n".join(messages)

        return result

    # ---------- MEMORY ----------
    if "memory" in task or "ram" in task:
        result = run_command(
            command_windows='systeminfo | findstr /C:"Total Physical Memory"',
            command_linux="free -m"
        )

        if result["os"] == "Windows":
            mem = format_windows_memory_output(result["output"])
            return f"Total Physical Memory: {mem}"

        return result

    # ---------- CPU ----------
    if "cpu" in task:
        result = run_command(
            command_windows="wmic cpu get loadpercentage",
            command_linux="top -bn1 | head -10"
        )

        if result["os"] == "Windows":
            cpu_load = format_windows_cpu_output(
                result["output"].splitlines()[-1]
            )
            status = "OK" if cpu_load < 80 else "HIGH ⚠️"
            return f"CPU Load: {cpu_load}% ({status})"

        return result

    return "System agent could not understand the task"
