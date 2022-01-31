import requests as rq
import json

base_currency = 'USD'
api_key = "8dec2eb0-827d-11ec-b089-ff084e189476"
rates = rq.get("https://freecurrencyapi.net/api/v2/latest?apikey={}&base_currency={}".format(api_key, base_currency))


print(rates)