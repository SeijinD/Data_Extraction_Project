import requests
from bs4 import BeautifulSoup
# lists of you need
links, links2, links_href, links2_href = [], [], ['https://en.wikipedia.org/wiki/Mia_Khalifa'], []
number = 2 # number limit for loop

def scrap(links_href):
    for link_href in links_href: # loop for all links in list
        page = requests.get(link_href) # get requests and save in var page
        soup = BeautifulSoup(page.content, 'html.parser') # maek soup object from page
        # search all tags "a" with attribute href and it start  with /wiki/ and has title
        for link in soup.find_all('a', href=lambda value: value and value.startswith("/wiki/"), title = True):
            full_href = "https://en.wikipedia.org" + link['href'] # correct links
            links2_href.append(full_href) # add in links2_href for after loop
            links.append(link['title'] + " - " + full_href) # add in links with title for print

        links2 = list(dict.fromkeys(links)) # delete duplicate for print
        links.clear() # clear previous list
        with open("log.txt", 'a', encoding='utf8') as f: # write all links of link in file
            for item in links2:    
                f.write(item +"\n")
    global number # get global number
    number -= 1 # -1 for the step
    if number != 0: # check number for call function again
        links_href = list(dict.fromkeys(links2_href)) # delete duplicate for scrap links again
        links2_href.clear() # clear previous list
        scrap(links_href) # call function

scrap(links_href) # call function for start program