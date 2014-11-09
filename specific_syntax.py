"""
DISPLAYING OUTPUT IN A SINGLE LINE
The , character after our print statement means that our next print statement keeps printing on the same line.
"""

phrase = "A bird in the hand..."

for i in phrase:
    if i=='a' or i == 'A':
        print 'X',
    else:
        print i,
        
"""
output        
X   b i r d   i n   t h e   h X n d . . .

"""

"""
ENUMERATE
enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the
loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop
with a list, except this gives us an easy way to count how many items we've seen so far.
"""

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for x, y in enumerate(choices): # x is the index (0 to 3 here) and y is the item in the list
    print x+1,y  #x+1 as index starts from 0 which we don't want the user to know.

"""
OUTPUT
Your choices are:
1 pizza
2 pasta
3 salad
4 nachos
"""
