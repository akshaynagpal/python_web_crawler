def anti_vowel(text):
    vowel_list = ['a','e','i','o','u','A','E','I','O','U']
    x = ""
    for i in text:
        if(i not in vowel_list):
            x += i
    return x  
