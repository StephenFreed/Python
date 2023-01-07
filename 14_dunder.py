# dunder methods are built in python object methods
# we can override these methods in our classes to get the functionality we want

class NoDunderOverrides:
    x = 5
    y = 10


print("~~~~~ No Dunder Override ~~~~~")
no_dunder = NoDunderOverrides
print(no_dunder)


class DunderOverride:
    x = 5
    y = 10

    # this overrides __init__ passing in self object and arguments to hold
    def __init__(self, name="no name yet", age="no age yet"):
        self.name = name
        self.age = age

    def __repr__(self):
        return "I Am DunderOverride Class"

    def __len__(self):
        return 99


print("~~~~~ Dunder Override ~~~~~")
duner_override = DunderOverride("Stephen")
print(duner_override)
print(len(duner_override))
print(duner_override.name)
print(duner_override.age)
