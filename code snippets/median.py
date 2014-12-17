def median(input_list):
    sorted_list = sorted(input_list)
    l = len(sorted_list)
    if(l%2 == 0):
        med = float (sorted_list[l/2] + sorted_list[(l/2)-1])/2
        return med
    else:
        med = sorted_list[l/2]
        return med
