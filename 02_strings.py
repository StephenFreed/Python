
"""
selecting characters from a strings, slicing strings, and concatenating strings. Each time we perform one of these operations we are creating an entirely new string.

This is because strings are immutable. This means that we cannot change a string once 
it is created. We can use it to create other strings, but we cannot change the string itself.

This property, generally, is known as mutability. Data types that are mutable can 
be changed, and data types, like strings, that are immutable cannot be changed.
"""


multi_line_string = """
        Space is held
    So you can format multi-line this way
line one \n line two
\tTabbing in
"""
# print(multi_line_string)

name = "My Name"

# PYTHON STRING METHODS
# print(len(name))
# print(name.capitalize())
# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.find("e"))
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("e"))
# print(name.replace("e", "O"))

string_to_strip = "      Foo      "
string_to_strip_comma = ",,,,,,Foo,,,,,,"
# print(string_to_strip.strip())
# print(string_to_strip_comma.strip(","))

string_to_split = "One, Two, Three"
# print(string_to_split.split(","))
make_string_list = ["One", " Two", " Three"]
# print(' '.join(make_string_list))


# STRING FORMATTING
print("This is a {}".format("formatted string"))
print("This {1} a {0}".format("formatted string", "is"))
print("This {two} a {one}".format(one="formatted string", two="is"))
print("The price is {:.2f}".format(49))
# f string is faster, but .format can be more readable
print(f"My name is {name}") 


# EXCAPE CHARACTER
escaped_char_string = "And I quote, \"This is a quote printed!\""
print(escaped_char_string)
