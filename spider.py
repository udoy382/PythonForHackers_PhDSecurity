# https://en.wikipedia.org/wiki/Programmer

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Programmer"

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.find_all('a'))
    # print(soup.find(id='Terminology'))

    var = soup.find(id="Count")
    # print(var)

    tag = soup.find_all("a")
    # print(tag)

    for t in tag:
        url2 = t.get('href')
        print(url2)


# user_input = input("Enter url would you like to scrape >  ")
get_page(url)