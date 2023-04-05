import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

base_url = 'https://cantorcristaobatista.com.br/CantorCristao/hino/show/'

first_hymn = 1
last_hymn = 581

hymns = []

for current_hymn in range(first_hymn, last_hymn + 1):
    print(f"{current_hymn}/{last_hymn}")
  
    driver.get(base_url + str(current_hymn))
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    h1 = soup.select('#k2Container > div.body > h1')
    title = h1[0].text.split(' - ')[1]
    lyrics = soup.select('#letra')[0].text

    hymns.append({ 
        'id': current_hymn,
        'title': title,
        'lyrics': lyrics
    })

with open('cantor_cristao.json', 'w') as outfile:
    json.dump(hymns, outfile)

driver.quit()

