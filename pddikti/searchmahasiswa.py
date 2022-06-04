import requests
import json
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("headless")
options.add_argument("log-level=3")
driver = webdriver.Edge(options = options)



baseurl = "https://api-frontend.kemdikbud.go.id/hit_mhs/"
search = input("Input Nama dan Universitas (Optional): ")

res = requests.get(baseurl+search)

data = json.loads(res.content)


for mahasiswa in data['mahasiswa']:
    dataurl = "https://pddikti.kemdikbud.go.id"+mahasiswa['website-link']

    driver.get(dataurl)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))


    biodata = driver.find_element(By.TAG_NAME, "tbody")
    arr = biodata.text.split("\n")
    print(arr)
    with open('result.txt', 'a') as f:
        f.write(str(arr))
        f.writelines('\n')

