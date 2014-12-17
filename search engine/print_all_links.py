def print_all_links(page):
	while page:
		url,endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
		return	
