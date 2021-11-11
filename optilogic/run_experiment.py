import os
import subprocess

try:
    result = subprocess.run("cd ../ && dvc exp run", shell=True, capture_output=True, check=True, cwd=os.getcwd())
    print(result.stdout.decode('utf-8'))
except subprocess.CalledProcessError as e:
    print(f'Experiment failed to run via DVC\n\n{e.stderr.decode("utf-8")}')