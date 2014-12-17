import urllib2
response = urllib2.urlopen('http://google.com/')
html = response.read()

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None,0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

def print_all_links(page):
	while page:
		url,endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			return	


print_all_links(html)