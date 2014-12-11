#function remove_duplicates takes in a list and removes elements of the list that are the same.

def remove_duplicates(input_list):
    result = []
    k = -1
    for i in input_list:
        k += 1
        flag = False
        for j in range(0,k,+1):
            if(input_list[j] == i):
                flag = True
        if(flag==False):
            result.append(i)
        else:
            continue
    return result
