import json
import random
import requests


server_url = 'http://localhost:8069'
db_name = 'odoo'
username = 'odoo'
password = 'odoo'

json_endpoint = "%s/jsonrpc" % server_url
headers = {"Content-Type": "application/json"}

def get_json_payload(service, method, *args):
    return json.dumps({
        "jsonrpc": "2.0",
        "method": 'call',
        "params": {
            "service": service,
            "method": method,
            "args": args
        },
        "id": random.randint(0, 1000000000),
    })

payload = get_json_payload("common", "version")
response = requests.post(json_endpoint, data=payload, headers=headers)

print(response.json())