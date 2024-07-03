import subprocess
import sys
import json

def execute_command(cmd):
    try:
        return subprocess.run(cmd, shell=True, check=True, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.STDOUT, 
                                text=True).stdout
    except subprocess.CalledProcessError as e:
        return e.output


scan_results = execute_command(f"nmap -sV -T4 -p- --top-ports 1000 {sys.argv[1]}")

print(
    json.dumps(
        {
            "type": "Tree",
            "results": [f"```\n{scan_results}\n```"],
        }
    )
)