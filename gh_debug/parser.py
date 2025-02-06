import subprocess

def get_github_logs(run_id=None):
    cmd = ["gh", "run", "view"]
    if run_id:
        cmd.append(str(run_id))
    else:
        cmd.append("--latest")
    cmd.append("--log")

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to get logs from GitHub Actions")
        return None
    return result.stdout
