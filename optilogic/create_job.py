import argparse
import json
import requests

parser = argparse.ArgumentParser(description='Create a new Optilogic Job')
parser.add_argument('--workspace', help='Optilogic Workspace Name')
parser.add_argument('--directoryPath', help='Optilogic Path to Directory')
parser.add_argument('--filename', help='Optilogic Path to Filename')
parser.add_argument('--api_key', help='Optilogic Token')

args = parser.parse_args()

url = f'https://dev.api.optilogic.app/v0/{args.workspace}/job?directoryPath={args.directoryPath}&filename={args.filename}'
headers = {
	'X-API-KEY': f'{args.api_key}'
	}

response = requests.request('POST', url, headers=headers)
job_object = json.loads(response.text)
try:
	job_key = job_object['jobKey']
	print(job_key)
except Exception as e:
	print(f'There was an error with getting the jobKey\n\nResponse: {job_object}')
