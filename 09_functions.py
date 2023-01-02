# Parameters & Arguments

def HelloWorld(name):
    """
    explain what this function does
    """
    print(f"Hello Word From {name}")

HelloWorld("Bob")


# keyword Arguments vs positional
# calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

# Here we are using a total of two built-in functions in our example: print(), and len()
help("string")
# https://docs.python.org/3/library/functions.html

# Here we are using a default value for our parameter of `destination` 
def trip_welcome(destination="California"):
    print(" Looks like you're going to ")
