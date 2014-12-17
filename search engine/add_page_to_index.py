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
    





add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
