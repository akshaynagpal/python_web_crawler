n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results=[]
    for lst in lists:
        for numbers in lst:
            results.append(numbers)
    return results

print flatten(n)
