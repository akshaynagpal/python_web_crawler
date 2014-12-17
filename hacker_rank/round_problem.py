# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159

#ENTER CODE BELOW HERE
str_x = str(x)
decimal_pos = str_x.find(".")
digit_after_decimal  = str_x[decimal_pos+1]
if int(digit_after_decimal)>4:
    print int(str_x[0:decimal_pos])+1
else:
    print int(str_x[0:decimal_pos])
