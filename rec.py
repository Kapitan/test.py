import requests

x = requests.get('https://api.github.com')
print(x.status_code)


