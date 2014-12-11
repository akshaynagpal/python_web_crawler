#function remove_duplicates takes in a list and removes elements of the list that are the same.

def remove_duplicates(input_list):
    result = []
    for i in input_list:
        flag = 0
        for j in range(0,i-1,1):
            if(input_list[j] == i):
                flag = 1
        if(flag==1):
            continue
        else:
            result.append(i)
    return result
