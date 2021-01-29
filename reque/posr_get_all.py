import requests

header = {
#    "Access-Control-Allow-Origin": "*",
    "Content-type": "application/json",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

data = {
    "draw": 1,
    "columns": [
        {
            "data": "transactionId",
            "name": "",
            "searchable": "true",
            "orderable": "true",
            "search": {"value": "", "regex": "false"},
        },
        {
            "data": "state",
            "name": "",
            "searchable": "true",
            "orderable": "true",
            "search": {"value": "", "regex": "false"},
        },
        {
            "data": "data",
            "name": "",
            "searchable": "true",
            "orderable": "true",
            "search": {"value": "", "regex": "false"},
        },
    ],
    "order": [{"column": 2, "dir": "desc"}],
    "search": {"value": "", "regex": "false"},
    "start": 0,
    "length": 5,
}


r = requests.post('https://testprocessingback.eva.ua/transactions/getAll', json=data)
# r = requests.post('http://10.255.253.40:8087/transactions/getAll', json=data)

print(r.text)
print(r.url)

