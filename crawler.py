import urllib2
from bs4 import BeautifulSoup

def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}   # <url>:[list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            c = BeautifulSoup(content)
            static_content = c.get_text()
            add_page_to_index(index, page, static_content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):  #Stanford's page rank algorithm's simplified implementation
    d = 0.8  # damping factor
    num_loops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0,num_loops):
        newranks = {}
        for page in graph:
            newrank = 1-d / npages
            #update by summing in the inlink ranks
            for node in graph:
                if page in graph[node]:
                    newrank += d*(ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


def get_page(page):
    response = urllib2.urlopen(page)
    html = response.read()
    return html

def get_all_links(page):
    links = []
    soup = BeautifulSoup(page,"lxml")
    for link in soup.find_all('a'):
        x = link.get('href')
        if x is not None:
            if x.find('http')==0:
                links.append(x)
    return links



def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word.lower(), url)

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)  # TO DO : check update instead of append
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


print "Web Crawler"
user_input = raw_input("(All websites wont work. Still under maintenance)\nEnter website to crawl (for eg. http://google.com) :")
print "Crawling Please wait"
index , graph = crawl_web(user_input)

ranks_returned = compute_ranks(graph)
for i in ranks_returned:
    print i + " " + str(ranks_returned[i])
print "website entered by user crawled"
print "keywords found are listed below:"
keyword_list = index.keys()
for keyword in keyword_list:
    print keyword
    
search_input = raw_input("enter search keyword:")

lookup_result = lookup(index,search_input.lower())

if lookup_result == None:
    print "Keyword not found"
else:

    for i in lookup_result:
        print i + " (Relevance : "+ str(ranks_returned[i]) +" )"

raw_input("press any key to exit")