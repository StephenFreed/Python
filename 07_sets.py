
"""
a set is a collection which is unordered, unchangeable*, and unindexed.
* Note: Set items are unchangeable, but you can remove items and add new items.
"""

my_set = {"foo", "bar", "baz", "foo"}
print(type(my_set))
print(my_set)

my_set_2 = {"abc", 34, True, 40, "male"}
print(my_set_2)

set_constructor = set(("apple", "banana", "cherry")) # note the double round-brackets
print(set_constructor)


my_set.add("new item")
print(my_set)
# remove() method will raise an error if the specified item does not exist, and the discard() method will not
my_set.remove("foo")
print(my_set)
# my_set.discard("something")
