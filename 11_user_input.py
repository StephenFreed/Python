
# get user input
likes_snakes = input("Do you like snakes? ")

print(f"Your Answer: {likes_snakes}\n")

# user input numbers into user_input variable.
user_input_numbers = input("Numbers:")

# creates list of str elements into list input_values_list.
input_values_list = user_input_numbers.split()
print(f"List of Inputs: {input_values_list}")
type_of_element_string = ""
for element in input_values_list:
    type_of_element_string+=str(type(element)) + " "
print(f"{type_of_element_string}\n")

# convert str elements from input_values_list to int in my_list.
my_list = []
for str_loop_value in input_values_list:
    my_list.append(int(str_loop_value))
print(f"{my_list}")
type_of_element_my_string = ""
for element in my_list:
    type_of_element_my_string+=str(type(element)) + " "
print(f"{type_of_element_my_string}\n")


