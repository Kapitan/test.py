import requests

h = {
    "accept": "application/json"
}

r = requests.get("http:///api/SimpleFile/GetSystemInfo", params=h)

print(r.json()[2]['systemName'])
