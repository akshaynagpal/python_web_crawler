def compute_ranks(graph):
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
