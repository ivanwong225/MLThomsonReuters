import json
import requests 

#Basic coindesk API hook

def get_request(price):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/" + price + ".json")
    j_obj = json.loads(response.text)
    print("As of " + j_obj["time"]["updated"] + ", the price of a Bitcoin in " + price + " is: " + j_obj["bpi"]["USD"]["rate"])


get_request("USD")
