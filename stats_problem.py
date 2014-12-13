# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
arr = [int(i) for i in raw_input().strip().split()]

mean = float (sum(arr)) / n
print mean

def calc_median(input_list):
    sorted_list = sorted(input_list)
    l = len(sorted_list)
    if(l%2 == 0):
        med = float (sorted_list[l/2] + sorted_list[(l/2)-1])/2
        return med
    else:
        med = sorted_list[l/2]
        return med
    
median = calc_median(arr)
print median

def mode(inp_list):
    sort_list = sorted(inp_list)
    dict1 = {}
    for i in sort_list:        
            count = sort_list.count(i)
            if i not in dict1.keys():
                dict1[i] = count
                
    maximum = 0 #no. of occurences
    max_key = -1 #element having the most occurences
    
    for key in dict1:
        if(dict1[key]>maximum):
            maximum = dict1[key]
            max_key = key 
        elif(dict1[key]==maximum):
            if(key<max_key):
                maximum = dict1[key]
                max_key = key
             
    return max_key

print mode(arr)

def std_deviation(arr,mean):
    
    sum_sqr_distances = 0
    float(sum_sqr_distances)
    
    for i in arr:
        sum_sqr_distances += (i-mean)**2
        
    std_dev = 0.0
    float(std_dev)
    std_dev = (sum_sqr_distances/n)**0.5
    
    return round(std_dev,1)

std_dev = std_deviation(arr,mean)
print std_dev

"""
95% confidence interval
------------------------
Lower limit = M - Z.95 M

Upper limit = M + Z.95 M

where,

M = mean
Z.95 = 1.96

M = standard error of mean = / (n^0.5)

where  = std. deviation
"""

def calc_confidence_interval(arr,mean,std_dev):
    std_error = float(std_dev/(len(arr)**0.5))
    
    lower = 0.0
    upper = 0.0
    lower = mean - (1.96 * std_error)
    upper = mean + (1.96 * std_error)
    print str(lower) + " " + str(upper)
    return 1

calc_confidence_interval(arr,mean,std_dev)

