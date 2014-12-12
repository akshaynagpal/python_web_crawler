"""
List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

[start:end:stride]
Where start describes where the slice starts (inclusive), end is where it ends (exclusive), and stride describes the space between items in the sliced list. For example, a stride of 2 would select every other item from the original list to place in the sliced list.
"""
my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]  #[1, 3, 5, 7, 9]

backwards = my_list[::-1]

print backwards  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
