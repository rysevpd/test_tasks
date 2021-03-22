import requests
from bs4 import BeautifulSoup


def get_count(url):
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
        print(i)
    dict_res={}
    for i in x:
        symbol = i[0]

        if dict_res.get(symbol) == None:
            dict_res[symbol] = 1
        else:
            ch = dict_res.get(symbol) + 1
            x = {symbol: ch}
            dict_res.update(x)
    return dict_res

