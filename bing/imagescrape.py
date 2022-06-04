from unittest import result
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import json
import os

search = input("Search Images: ")
parameter = {"q": search}
baseUrl = 'https://bing.com/images/search?q=' + search + '&safeSearch=off'
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}


result = requests.get(baseUrl, params=parameter, headers=headers)

bs = BeautifulSoup(result.text, "html.parser")

list = bs.find_all("a", {"class": "iusc"})
num = 1
os.makedirs(search)
for item in list:
    imglist = requests.get(json.loads(item.attrs["m"])['murl'])
    try:
        img = Image.open(BytesIO(imglist.content))
    except:
        print(img)
    img.save("./" + search + "/" + str(num) +"."+ img.format, img.format)
    print(num, "Images Downloaded")
    num = num + 1