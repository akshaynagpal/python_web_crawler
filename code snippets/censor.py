#censor takes two strings, text and word, as input. 
#It returns the text with the word you chose replaced with asterisks.

def censor(text,word):
    result = ""
    count = 0
    no_of_stars = 0
    split_list = text.split()
    for i in split_list:
        count += 1
        if(i==word):
            result += "*" * len(i)
        else:
            result +=i
        if(count != len(split_list)):
            result += " "    
    return result       
