import urllib2

def get_page(page):
    response = urllib2.urlopen(page)
    html = response.read()
    return html



def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None,0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        if url.find("http") != -1:
            return url, end_quote
        else:
            return None,end_quote



def get_all_links(page):
    links = []
    while page:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links      
  


def add_page_to_index(index,url,content):
    word_list = content.split()
    for word in word_list:
        flag = 0
        for lists in index:
            if lists[0]==word:
                flag = 1
                lists[1].append(url)
        if flag == 0:
           index.append([word,[url]])
    return       



def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)



def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            union(tocrawl,get_all_links(content))
            crawled.append(page)
            add_page_to_index(index,page,content)           
    return index

print "Web Crawler"
user_input = raw_input("(All websites wont work. Still under maintenance)\nEnter website to crawl (for eg. http://google.com) :")

result = crawl_web(user_input)

for i in result:
    print i
    print "\n"

raw_input("Thank you for using. Press any key to exit")