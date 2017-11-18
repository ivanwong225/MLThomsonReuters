import json
import requests
import datetime
from decimal import Decimal

#Basic coindesk API hook
#Need to convert pastPrices to 2-D Array of Time / Price

def getCurrentPrice():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
    j_obj = json.loads(response.text)
    x = j_obj["bpi"]["USD"]["rate"]
    return Decimal(x.replace(",", ""))

def getPastPrices(months): 
    today = datetime.date.today()
    startDate = today - datetime.timedelta(months*365/12)
    endDate = today - datetime.timedelta(1)
    response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json?start=" + str(startDate) + "&end=" + str(endDate))
    j_obj = json.loads(response.text)
    pastPrices = j_obj["bpi"]
    #2D Array Conversion
    PP_array = []
    for key, value in pastPrices.items():
        PP_array.append([key, value])
    print(PP_array) #Need to convert pastPrices to 2-D Array of Time / Price

#Test
getPastPrices(1)
