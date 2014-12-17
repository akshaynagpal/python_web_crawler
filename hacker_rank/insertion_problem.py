"""
Insert element into sorted list 
https://www.hackerrank.com/challenges/insertionsort1

Sample Input

5
2 4 6 8 3

Sample Output

2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
"""
#!/bin/python
def insertionSort(ar):  
    l = len(ar)
    ele = ar[l-1]
    i = l-2
    while ele < ar[i] and i>-1:
        ar[i+1] = ar[i]
        print str(ar).replace('[','').replace(']','').replace(',','')
        i -= 1
    if i==-1:
        ar[0]  = ele
    else:
        ar[i+1] = ele
    
    print str(ar).replace('[','').replace(']','').replace(',','')
    return 1

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
