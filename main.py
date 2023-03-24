import requests
from bs4 import BeautifulSoup

get_info = str()
get_search_info = input("Введіть пошукову фразу: ")
if get_search_info:
    get_info = get_search_info.split(" ")
else:
    print("None")

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

url = "https://freelancehunt.com/ua/freelancers?q={}&country=&city=".format("+".join(get_info))
response = requests.get(url, headers= headers)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)
