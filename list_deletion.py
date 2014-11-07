n = [1, 3, 5]
# Removing the first item in the list here

# n.pop(index) will remove the item at index from the list and return it 
print "item popped is"
print n.pop(0)
print n

#n.remove(item) will remove the actual item if it finds it
n.remove(3)

print n

#del(n[index]) is like .pop in that it will remove the item at the given index, but it won't return it

del(n[0])

print n
