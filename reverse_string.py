# reverse a string in python without using reversed() or [::-1]

def reverse(test):
    n = len(test)
    x=""
    for i in range(n-1,-1,-1):
        x += test[i]
    return x
