import requests
import json


url = "http://api.forismatic.com/api/1.0/"
# url = "https://www.ebi.ac.uk/chembl/api/utils/spore"
parametr = {
    "method": "getQuote",
    "format": "json",
    "key": 1,
    "lang": "ru"
}
r = requests.get(url, params=parametr)

print(r.json())

#quote = r.json()
# quote_text = quote["quoteText"]
# quote_author = quote["quoteAuthor"]
#print(quote)
# print(r)

