import json
import requests
import datetime
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as spcs
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
    #Use i to represent day instead of using actual date
    #actual date is a string and not easy to read on graph
    i = 1
    for key, value in pastPrices.items():
        PP_array.append([i, value])
        i += 1

    return PP_array
    #print(PP_array) Need to convert pastPrices to 2-D Array of Time / Price

def linearRegression(X, y):
	values = spcs.mstats.linregress(X, y)
	slope, intercept = values[0], values[1]
	linearFunc = lambda x: slope * x + intercept
	y2 = list(map(linearFunc, X))
	plt.plot(X, y, 'ro')
	plt.plot(X, y2, 'r--')
	plt.xlim(0, len(X))
	plt.show()
	
	return [slope, intercept]

#Gets data for past 3 months
#Test
data = getPastPrices(3)
#Presents data as an array instead of list
data = np.asarray(data)
X,y = data[:, 0, np.newaxis], data[:, 1, np.newaxis]
X = X.astype(int)

#Test
print(linearRegression(X, y))


