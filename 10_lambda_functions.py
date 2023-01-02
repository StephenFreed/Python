# useful to sort and filter data

# assign variable to lambda
my_func = lambda s: s * 2  # noqa
print(my_func(5))

# lambda with mulitple inputs
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()  # noqa
print(full_name("   stephen", "FREED"))

# tuple to hold different lambas
func_switch = (lambda x: x + 1, lambda x: x - 1)
x = 0
# func switch changes lambda calls on parent for loop idx
for i in range(2):
    for j in range(5):
        x = func_switch[i](x)
        print("* "*x)

# lambda to sort on last name
names = ["Jimmy Bob", "stephen freed", "joe adam", "someone zee", "bob cat"]
names.sort(key=lambda name: name.split(" ")[-1].lower())
new_names = [name.title() for name in names]
print(names)
print(new_names)
