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
			union(tocrawl,get_all_links(content))
			crawled.append(page)
			content = get_page(page)
			add_page_to_index(index,page,content)
			
	return crawled