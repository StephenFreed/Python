import sys

"""
generator is an object iterator
this is less memory than a data structure in memory
doesn't load entire data structure into memory at one time
"""

print("~~~~~ List Comprehension ~~~~~")
x = [num for num in range(1, 11)]
print(x)
print(sys.getsizeof(x))

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("~~~~~ List Structure ~~~~~")
print(y)
print(sys.getsizeof(y))
# print(next(y))  # error list object not an iterator

# this is an iterator
z = map(lambda z: z**2, y)

print("~~~~~ Map Generator ~~~~~")
print("~~~~~ Next Function ~~~~~")
print(next(z))
print(z.__next__())  # same as next function
print(next(z))
print(next(z))

print("~~~~~ Start Of For Loop ~~~~~")
# starts at 4th index
for num in z:
    print(num)

# this is what a for loop really is
# infinite loop through structure since we don't know how many iterations
print("~~~~~ Example What A For Loop Really Is ~~~~~")

# doesn't store list in memory, so have to call generator again to for loop again
z = map(lambda z: z**2, y)
while True:
    try:
        value = next(z)
        print(value)

    except StopIteration:
        print("Done")
        break

# things like range use iter() in the background to create a generator object
# iter()
# .__iter__()

# yield essentially uses the next() and iter() yielding result / yield creates generator
# execution pauses and prints element, then continues
print("~~~~~ Yield ~~~~~")


def my_generator(x):
    for i in range(x):
        yield i


for i in my_generator(5):
    print(i)

print("~~~~~ Manual Yield ~~~~~")
# manually calling
my_gen = my_generator(5)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


print("~~~~~ Generator Comprehension ~~~~~")

gen_comp = (i for i in range(20))
print(gen_comp)
