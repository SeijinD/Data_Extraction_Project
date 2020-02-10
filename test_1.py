import requests
from bs4 import BeautifulSoup
import io

page = requests.get('https://www.iee.ihu.gr/udg_courses')
soup = BeautifulSoup(page.content, 'html.parser')

# Lists to store the scraped data in
courses = []

# Extract data
table_7 = soup.findAll('table')[6]
for tr in table_7.findAll('tr'):
    for td in tr.findAll('td', {"title" : True}):
        if td['title']:
            courses.append(td['title'])
            with io.open("log.txt", 'a', encoding='utf8') as f:
                f.write(courses[-1]+"\n")
