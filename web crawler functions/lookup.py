def lookup(index,keyword):
    flag = 0
    for lists in index:
        if lists[0]==keyword:
            flag = 1
            return lists[1]
        
    if(flag==1):
        l = []
        return l
    

print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']
