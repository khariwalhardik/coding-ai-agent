import os
import sys
import subprocess
from typing import Optional

def run_python_file(working_dir: str, file_path: str) -> str:
    """
    Run a Python file in a given working directory and capture its output.
    Returns stdout if successful, otherwise returns error message.
    """
    # Resolve absolute path
    target_file = os.path.abspath(os.path.join(working_dir, file_path))
    if not os.path.isfile(target_file):
        return f"File does not exist: {target_file}"

    try:
        # Use sys.executable for correct Python interpreter
        result = subprocess.run([
            sys.executable, target_file
        ], capture_output=True, text=True, cwd=working_dir, timeout=10)
        output = result.stdout
        error = result.stderr
        if result.returncode != 0:
            # Return both stdout and stderr for debugging
            return f"Error running file (exit code {result.returncode}):\nSTDOUT:\n{output}\nSTDERR:\n{error}"
        return output
    except Exception as e:
        return f"Exception occurred: {str(e)}"