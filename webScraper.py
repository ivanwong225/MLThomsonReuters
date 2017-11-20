from bs4 import BeautifulSoup
import requests
import time
from random import randint


def scrape_news_summaries(s):
    time.sleep(randint(0, 2))  # relax and don't let google be angry
    r = requests.get("http://www.google.com/search?q="+s+"&tbm=nws")
    print(r.status_code)  # Print the status code
    content = r.text
    news_summaries = []
    soup = BeautifulSoup(content, "html.parser")
#    titles = soup.findAll("h3", {"class":"r"})  #actual titles
    titles = soup.findAll("div", {"class": "st"}) #first sentences, kinda more like a headline
    for title in titles:
        news_summaries.append(title.text)
    return news_summaries


l = scrape_news_summaries("bitcoin") #replace param for keyword
for n in l:
    print(n)
    print()
