# import libs
import requests
from bs4 import BeautifulSoup

# lists for my data
links = []
full_hrefs = []

# scrap function
def scrap(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'html.parser')

    for index, link in enumerate(soup.find_all('a', href=lambda value: value and value.startswith("/wiki/"), title = True), start = 1):
        full_href = "https://el.wikipedia.org" + link['href']
        full_hrefs.append(full_href)
        links.append(str(index) + " - " + link['title'] + " - " + full_href)     
    
    # print links list
    with open("log.txt", 'a', encoding='utf8') as f:
        for item in links:    
            f.write(item +"\n")

    # run function for every link in links
    for href in full_hrefs:
        scrap(href)

    # clear list if finished a list
    full_hrefs.clear()

# call function      
scrap('https://el.wikipedia.org/wiki/%CE%94%CE%B9%CE%B5%CE%B8%CE%BD%CE%AD%CF%82_%CE%A0%CE%B1%CE%BD%CE%B5%CF%80%CE%B9%CF%83%CF%84%CE%AE%CE%BC%CE%B9%CE%BF_%CF%84%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%BF%CF%82')