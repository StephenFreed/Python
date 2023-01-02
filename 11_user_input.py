

import os

answer = os.environ.get("TEST_USER")

print(answer)

likes_snakes = input("Do you like snakes? ")

# User input numbers into user_input variable.
user_input = input('Numbers:')

# Creates list of str elements into list input_values_list.
input_values_list = user_input.split()

print()
print(input_values_list)

# Convert str elements from input_values_list to int in my_list.
my_list = []
for str_loop_value in input_values_list:
    my_list.append(int(str_loop_value))

print(my_list)

#print out numbers from my_list with negatives as 0.
for my_list_index, my_list_element in enumerate(my_list):
    if my_list_element < 0:
        my_list[my_list_index] = 0

for final_values in my_list:
    print(final_values, end=' ')
print()

