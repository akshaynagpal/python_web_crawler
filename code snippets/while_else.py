"""
WHILE / ELSE 
Something completely different about Python is the while/else construction. while/else is similar to if/else, but there is a 
difference: the else block will execute anytime the loop condition is evaluated to False. This means that it will execute if
the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be 
executed.
"""

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else: #this will work if while exits normally. It won't be executed if while is exited due to a break statement.
    print "You win!"
 
"""
FOR/ELSE LOOP 
Just like with while, for loops may have an else associated with them.
In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break. 
"""
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

"""
OUTPUT
You have...
A banana
A apple
A orange
A tomato is not a fruit!
"""

