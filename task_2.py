import requests
from bs4 import BeautifulSoup


"""
Сначала получаем html первой страницы.
Цикл while работает по принципу - есть следующая страница - действуем.
Как только доходим до последней страницы - скрипт останавливается.
"""

def get_count(url, dict_res):
    """
    Данная функция получает на вход url страницы для парсинга, а также словарь с итоговым списком.
    Сначала она получает и заносит в txt список животных, после чего проходит и в соответсвии в 
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    f = open("words.txt", "w")
    soup = soup.find_all("ul")
    for i in soup:
        if i.text == "":
            break
        f.write(i.text + "\n")


    with open('words.txt', 'r') as f:
        nums = f.read().splitlines()
    x = nums[2:-3]
    
    for i in x:
        symbol = i[0]
        if dict_res.get(symbol) == None:
            dict_res[symbol] = 1
        else:
            ch = dict_res.get(symbol) + 1
            x = {symbol: ch}
            dict_res.update(x)
    return dict_res

url_start = ("https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2" \
             "%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83")
url_begin = "https://ru.wikipedia.org"

dict_res={}
dict_res = get_count(url_start, dict_res)
# dict_result_sum.update(x)
page = requests.get(url_start)
soup = BeautifulSoup(page.text, "html.parser")
teg_a_res = soup.findAll('a')
page_num = 1  # для теста
for data in teg_a_res:
    if data.text == "Следующая страница":
        result = data.get("href")
        break

while result != 0:
    print("страница ", page_num)
    url = url_begin + result
    result = 0
    page_num += 1  # для теста
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    dict_res = get_count(url, dict_res)
    #dict_result_sum.update(x)

    teg_a_res = soup.findAll('a')

    for data in teg_a_res:
        if data.text == "Следующая страница":
            result = data.get("href")
            break


print(dict_res)

for k in sorted(dict_res.keys()):
    print (k, ':', dict_res[k])
