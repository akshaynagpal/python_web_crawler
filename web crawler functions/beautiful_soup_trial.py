import urllib2
from bs4 import BeautifulSoup


def get_page(page):
    response = urllib2.urlopen(page)
    html = response.read()
    return html

markup = get_page("http://www.google.com")

soup = BeautifulSoup(markup,"lxml")

#print soup.prettify()

for link in soup.find_all('a'):
    x = link.get('href')
    if x.find('http')==0:
        print x