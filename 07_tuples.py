"""
a tuple is a collection which is ordered and unchangeable after creation
"""

# need a comma
my_tuple = ("foo",)
print(type(my_tuple))

# not a tuple
my_string = ("foo")
print(type(my_string))

my_tuple_2 = tuple(("foo", "foo", "bar", "baz")) # note the double round-brackets
print(my_tuple_2 )


print(my_tuple_2.count("foo"))
print(my_tuple_2.index("Bar"))

