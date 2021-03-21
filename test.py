import requests
from bs4 import BeautifulSoup

"""
Сначала получаем html первой страницы.
Цикл while работает по принципу - есть следующая страница - действуем.
Как только доходим до последней страницы - скрипт останавливается.
"""
url_start = ("https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2" \
             "%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83")
url_begin = "https://ru.wikipedia.org"
page = requests.get(url_start)
soup = BeautifulSoup(page.text, "html.parser")
# print(page.text)

# teg_a_res = soup.findAll('ul')
# print(teg_a_res)

soup = soup.find_all("ul")
for i in soup:
    print(i.text)