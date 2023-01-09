# get a list of integers from the user with list comprehension.
numbers = [int(i) for i in input('Enter numbers:').split()]

# creates list of even numbers. int important.
even_numbers = [i for i in numbers if (i % 2) == 0]

# changes list from integers to string.
even_numbers = [str(i) for i in even_numbers]

# join won't work unless string type.
print('Even numbers only:', even_numbers)
print(','.join(even_numbers))
