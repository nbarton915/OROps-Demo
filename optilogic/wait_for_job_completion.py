from install_requirements import ensure_requirements
ensure_requirements()

import argparse
import json
import requests
import time

parser = argparse.ArgumentParser(description='Create a new Optilogic Job')
parser.add_argument('--workspace', help='Optilogic Workspace Name')
parser.add_argument('--jobKey', help='Optilogic Path to Directory')
parser.add_argument('--api_key', help='Optilogic Token')

args = parser.parse_args()

url = f'https://api.optilogic.app/v0/{args.workspace}/job/{args.jobKey}?op=status'
headers = {
	'X-API-KEY': f'{args.api_key}'
	}

complete_status_list = ['done', 'error', 'cancelled', 'stopped']
job_status = None
while job_status not in complete_status_list:
    time.sleep(5)
    try:
        response = requests.request('GET', url, headers=headers)
        job_object = json.loads(response.text)
        job_status = job_object['status']
    except Exception as e:
        print(f'There was a problem getting the job status. No longer checking for safety sake\n\n{job_object}')
        raise
print(job_status)
