import requests 
import socket
import json
from rich.console import Console 


## Obtention du hostname + adresse ip de la machine
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")


## Déclaration des variables relative aux requêtes http afin de manipuler zabbix

console = Console()
token = None
api_url = "http://adresse.ip/zabbix/api_jsonrpc.php"
headers = {"Content-Type": "application/json-rpc" }


# On récupère le token d'auth 

if token == None:
    data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "password"
    },
    "id": 1,
    "auth": None
    }
    r = requests.post(api_url, headers=headers, json = data)

console.print_json(data=r.json())



# Création de l'host

host_create = [
{
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": hostname,
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip_address,
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10326"
            }
        ]
        },
        "auth": "d82e6f506c99ea25b0b5edadd03de531",            
        "id": 1
}
]

r_host = requests.post(api_url, headers=headers, json = host_create)

console.print_json(data=r_host.json())
