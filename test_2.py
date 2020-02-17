import requests
from bs4 import BeautifulSoup

links = []
full_hrefs = []

def scrap(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')
    for index, link in enumerate(soup.find_all('a', href=lambda value: value and value.startswith("/wiki/"), title = True), start = 1):
        full_href = "https://el.wikipedia.org" + link['href']
        full_hrefs.append(full_href)
        links.append(str(index) + " - " + link['title'] + " - " + full_href)     
        with open("log.txt", 'a', encoding='utf8') as f:
            f.write(links[-1]+"\n")
    for href in full_hrefs:
        scrap(href)
    full_hrefs.clear()
        
scrap('https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B5%CE%B8%CE%BD%CE%AD%CF%82_%CE%A0%CE%B1%CE%BD%CE%B5%CF%80%CE%B9%CF%83%CF%84%CE%AE%CE%BC%CE%B9%CE%BF_%CF%84%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%BF%CF%82')