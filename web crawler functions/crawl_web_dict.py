def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)



def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = {}
	graph = {}
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index,page,content)
			outlinks = get_all_links(content)
			graph[page] = outlinks
			union(tocrawl,outlinks)
			crawled.append(page)	
	return index, graph