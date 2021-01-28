import requests
#
# header = {
#     "Access-Control-Allow-Origin": "*",
#     "Content-type": "application/json",
#     "Cache-Control": "no-cache",
#     "Pragma": "no-cache"
# }
# data = {
#  "draw": 1,
#  "columns": [
#     {
#      "data": "transactionId",
#      "name": "",
#      "searchable": "true",
#      "orderable": "true",
#      "search": { "value": "", "regex": "false" },
#    },
#    {
#      "data": "state",
#      "name": "",
#      "searchable": "true",
#      "orderable": "true",
#      "search": { "value": "", "regex": "false" },
#    },
#    {
#      "data": "data",
#      "name": "",
#      "searchable": "true",
#      "orderable": "true",
#      "search": { "value": "", "regex": "false" },
#    },
#  ],
#  "order": [{ "column": 2, dir: "desc" }],
#  "search": { "value": "", "regex": "false" },
#  "start": 0,
#  "length": 5,
# }
# r = requests.post('https://testprocessingback.eva.ua/transactions/getAll',json=data, headers=header)
#
# print(r.text)

header = {
    "Access-Control-Allow-Origin": "*",
    "Content-type": "application/json",
    "Cache-Control": "no-cache, no-store, max-age=0, must-revalidate",
    "Pragma": "no-cache"
}

#jjson = {"dataTablesParameters":{"draw":1,"columns":[{"data":"planogramPhotoId","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}},{"data":"planogramInfoEntity.phone","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}},{"data":"planogramInfoEntity.locationInfoEntity.filial","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}},{"data":"planogramInfoEntity.locationInfoEntity.region","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}},{"data":"planogramInfoEntity.locationInfoEntity.shopName","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}},{"data":"planogramInfoEntity.date","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}},{"data":"categoryEntity.text","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}},{"data":"photo","name":"","searchable":"true","orderable":"true","search":{"value":"","regex":"false"}}],"order":[{"column":5,"dir":"desc"}],"start":0,"length":5,"search":{"value":"","regex":"false"}},"userRoles":[]}


r = requests.post("https://testdt.eva.ua/categoris", data=[], headers=header)

print(r.content)
