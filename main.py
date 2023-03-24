import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.google.com/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

url = "https://freelancehunt.com/ua/projects/skill/1c/56.html"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

all_info = dict()
price = int()
head = str()
data = str()
heads = soup.find_all("td", class_='left')

for elem in range(0, len(heads)):
    try:
        try:
            if heads[elem].find("div", class_="text-green price with-tooltip").text.strip():
                price = heads[elem].find("div", class_="text-green price with-tooltip").text.strip()
        except AttributeError:
            price = "Не вказано"
        elements = {
            "Посилання": heads[elem].find('a').get('href'),
            "Заголовок" : heads[elem].find('a').get('title'),
            "Опис": heads[elem].find("p").text.strip(),
            "Ціна" : price,
        }
        all_info[elem] = elements
    except AttributeError as a:
        pass





