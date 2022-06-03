import requests 
import json
from rich.console import Console 

console = Console()
token = None
api_url = "http://192.168.1.57/zabbix/api_jsonrpc.php"
headers = {"Content-Type": "application/json-rpc" }


if token == None:
    data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1,
    "auth": None
    }
    r = requests.post(api_url, headers=headers, json = data)

console.print_json(data=r.json())
