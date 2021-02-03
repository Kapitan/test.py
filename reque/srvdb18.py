import requests

h = {
    "accept": "application/json"
}

r = requests.get("http://srvdb18:5000/api/SimpleFile/GetSystemInfo", params=h)

print(r.json()[2]['systemName'])
