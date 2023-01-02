# this is a line comment

'''
this is a docstring
'''


"""
python is space sensative

Errors
syntaxerror is something wrong with the way your program is written
a nameerror occurs when the python interpreter sees a word it does not recognize
typeerror is an error thrown when an operation is applied to an object of an inappropriate type
logic error is an error found by the programmer when the program isn’t doing what it is intending to do
"""


# STRINGS
string_variable = "string 1"
string_variable_2 = 'string 1'
string_variable_2+=" and string 2"
# print(string_variable_2)


# NUMBERS
integer_variable = 5
float_variable = 4.1


# TYPES AND CASTING
# python has the following data types built-in by default, in these categories:
# text type:	str
# numeric types:	int, float, complex
# sequence types:	list, tuple, range
# mapping type:	dict
# set types:	set, frozenset
# boolean type:	bool
# binary types:	bytes, bytearray, memoryview
# none type:	nonetype

type_variable = 9
# print(type(type_variable))
# print(type_variable)
type_variable = str(type_variable)
# print(type(type_variable))
# print(type_variable)
type_variable = float(type_variable)
# print(type(type_variable))
# print(type_variable)


# CALULATIONS
# +, -, *, **, /, //, %, 
# print("5 + 2")
# print(5 + 2)
# print("5 - 2")
# print(5 - 2)
# print("5 * 2")
# print(5 * 2)
# print("5 ** 2")
# print(5 ** 2)
# print("10 / 7")  # python converts all ints to floats before performing division
# print(10 / 7)
# print("10 // 7")  # floor division
# print(10 // 7)
# print("12 % 10")
# print(12 % 10)


# BOOLEAN VARIABLES
boolean_true = True
boolean_false = False

# BOOLEAN EXPRESSIONS
boolean_var_1 = 3 != 3
boolean_var_2 = (3 - 3) == 0
boolean_var_3 = 1
boolean_var_4 = 0


# PYTHON OPERATORS PRECEDENCE RULE
# P – Parentheses
# E – Exponentiation
# M – Multiplication
# D – Division
# A – Addition
# S – Subtraction

# RELATIONAL OPERATORS
# == , !=, >, <, >=, <=

# CONTROL FLOW
# if, elif, else statement
# if (5 > 5):
#     print(5)
# if (10 > 5):
#     print(10)
# if (10 != 5):
#     print(10)

user_name = "Foo"
# if user_name == "Foo":
#     print("user_name was true")
# elif user_name == "Bar":
#     print("Bar was True")
# elif user_name == "Baz":
#     print("Baz was True")
# else:
#     print("All False")

# BOOLEAN OPERATORS
# if user_name == "Foo" and 3 == 3:
#     print("true")
#
# if user_name == "Bar" or 3 == 3:
#     print("true")

not_boolean = not 1 + 1 == 2  # prints opposite
# print(not_boolean)

little_string = "and"
big_string = 'amanda'
# if little_string in big_string:
    # print(True) 


