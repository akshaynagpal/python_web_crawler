# procedure add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    flag = 0
    count = 0
    for lists in index:
        if(lists[0]==keyword): 
            flag = 1
            index[count][1].append(url)
        count += 1
        
    count = 0        
    if(flag == 0):
        index.append([keyword,[url]])   


add_to_index(index,'udacity','http://udacity.com')
print index
add_to_index(index,'udacity','http://mmnpr.org')
print index
add_to_index(index,'computing','http://acm.org')
print index
add_to_index(index,'udacity','http://npr.org')
print index

"""
output
[['udacity', ['http://udacity.com']]]
[['udacity', ['http://udacity.com', 'http://mmnpr.org']]]
[['udacity', ['http://udacity.com', 'http://mmnpr.org']], ['computing', ['http://acm.org']]]
[['udacity', ['http://udacity.com', 'http://mmnpr.org', 'http://npr.org']], ['computing', ['http://acm.org']]]
"""

"""
answer code
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])
"""    
    
