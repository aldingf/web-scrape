from unittest import result
from bs4 import BeautifulSoup
import requests


search = input("Search anything: ")
pages = input("How many pages: ")

num = 1

for x in range(int(pages)):
    url = "https://www.bing.com/search"
    parameter = {"q": search, "first": num}
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    headers = {"user-agent": USER_AGENT}

    result = requests.get(url, params=parameter, headers=headers)

    scraper = BeautifulSoup(result.text, "html.parser")

    ol = scraper.find("ol", {"id": "b_results"})
    li = ol.findAll("li", {"class": "b_algo"})

    for item in li:
        print(item.find("a").text, ",", item.find("cite").text)
    num += 10
