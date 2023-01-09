
# ~~~~~~~~~~ functions are objects ~~~~~~~~~~
# python program to illustrate functions can be passed as arguments to other functions
print("~~~~~~~~~~ functions are objects ~~~~~~~~~~")


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


# passing functions as argument to change func
def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print(greeting)


greet(shout)
greet(whisper)


# ~~~~~~~~~~ decorator chaining ~~~~~~~~~~
# code for testing decorator chaining
print("~~~~~~~~~~ decorator chaining ~~~~~~~~~~")


def decor1(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper


def decor(func):
    def wrapper():
        x = func()
        return 2 * x
    return wrapper


# matters which decorator is first // nested calls in order
@decor1
@decor
def num():
    return 10


print(num())
print(decor(num)())  # must add () to wrapper object that is returned
print(decor1(num)())
# decorator similar to this call
print(decor1(decor(num))())  # must comment out decorators to get correct result

# function aliasing
x = decor1(decor(num))
x()


# ~~~~~~~~~~ decorator normal usage ~~~~~~~~~~
# code for using a wrapper function to return desired results
print("~~~~~~~~~~ decorator normal usage ~~~~~~~~~~")


def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")

    return wrapper


@f1
def f(a, b):
    print(f"({a}) is first arg / ({b}) is second arg")


f("Hi!", 9999)
