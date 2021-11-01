import os
import subprocess

def ensure_requirements():
    result = subprocess.run(f'pip3 install -r {os.getcwd()}/requirements.txt', capture_output=True, shell=True)
    result.check_returncode()
    print(result.stdout)
