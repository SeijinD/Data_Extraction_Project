import requests
from bs4 import BeautifulSoup

links, links_href, links2_href = [], ['https://en.wikipedia.org/wiki/Mia_Khalifa'], []
number = 2

def scrap(links_href):
    for link_href in links_href:
        page = requests.get(link_href)
        soup = BeautifulSoup(page.content, 'html.parser')

        for link in soup.find_all('a', href=lambda value: value and value.startswith("/wiki/"), title = True):
            full_href = "https://en.wikipedia.org" + link['href']
            links2_href.append(full_href)
            links.append(link['title'] + " - " + full_href)

        links2 = list(dict.fromkeys(links))
        links.clear()
        with open("log.txt", 'a', encoding='utf8') as f:
            for item in links2:    
                f.write(item +"\n")
    global number 
    number -= 1
    if number != 0:
        links_href = list(dict.fromkeys(links2_href))
        links2_href.clear()
        scrap(links_href)

scrap(links_href)