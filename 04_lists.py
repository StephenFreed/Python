

"""
4 built-in data types in python used to store collections of data list, set, tuple, and dictionary

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

lists can contain any mix of data type

example syntax for methods
list.method(input)

Example syntax for a built-in function 
builtinfuncion(input)
"""


# CONCATENTATE TWO LISTS
heights = [5, 6, 7, 8]
heights = heights + [9, 10, 11]
print(heights)


# CHANGE LIST
heights[1] = 55

heights.append(12)
print(heights)

heights.remove(11)
print(heights)

heights.insert(0, 100)
print(heights)

heights.pop()
print(heights)

heights.sort()  # in place
print(heights)

heights.sort(reverse=True)  # in place
print(heights)

sorted_heights = sorted(heights)  # creates new list
print(sorted_heights)


# list indexes
print(heights[0])  # first index
print(heights[-1])
print(heights[:4])  # exclusive
print(heights[2:])  # inclusive


# 2D list
twoD_list = [["Foo", 10], ["Bar", 20]]
print(twoD_list[0])
print(twoD_list[1])
print(twoD_list[1][0])

