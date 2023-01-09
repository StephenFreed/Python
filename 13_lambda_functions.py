"""
lambda function is a small anonymous function.
lambda function can take any number of arguments, but can only have one expression
useful to sort and filter data
"""

# assign variable to lambda
my_lambda = lambda s: s * 2
print(my_lambda(5))

# lambda with mulitple inputs
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   foo", "BAR"))

# tuple to hold different lambas
func_switch = (lambda x: x + 1, lambda x: x - 1)
x = 0
# func switch changes lambda calls on parent for loop idx
for i in range(2):
    for j in range(5):
        x = func_switch[i](x)
        print("* "*x)

# lambda to sort on last name
names = ["Jimmy Bob", "Foo Bar", "Joe Adam", "Same Zee", "Bob Cat"]
print(names)
names.sort(key=lambda name: name.split(" ")[-1].lower())
new_names = [name.title() for name in names]
print(new_names)
