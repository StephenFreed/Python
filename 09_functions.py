# Parameters & Arguments
# Function Signature

def hello_world(name):
    """
    this function adds argument name to hello world
    """
    print(f"Hello Word From {name}")


def trip_welcome(destination="California"):
    """
    default value for our parameter of "destination" 
    """
    print(f"Looks like you're going to {destination}")


hello_world("Foo")
trip_welcome("Florida")
trip_welcome()


def unknown_arguments_function(*names):
    """
    *args

    if you do not know how many arguments that will be passed into your function
    add a * before the parameter name in the function definition.

    this way the function will receive a tuple of arguments, and can access the items accordingly
    """
    name_list = []
    for name in names:
        name_list.append(name)

    print(name_list)

unknown_arguments_function("Foo", "Bar", "Baz")


def unknown_key_value_function(**names):
    """
    **kwargs

    if you do not know how many keyword arguments that will be passed into your function
    add two asterisk ** before the parameter name in the function definition.

    this way the function will receive a dictionary of arguments, and can access 
    the items accordingly
    """
    for key, value in names.items():
        print(f"{key}: {value}")

unknown_key_value_function(foo = "bar", bar = "foo", baz = "bar")
