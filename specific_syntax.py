The , character after our print statement means that our next print statement keeps printing on the same line.

phrase = "A bird in the hand..."

for i in phrase:
    if i=='a' or i == 'A':
        print 'X',
    else:
        print i,
        
/*output        
X   b i r d   i n   t h e   h X n d . . .

*/
