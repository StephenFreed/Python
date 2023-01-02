# FOR LOOP
print("~ For Loop ~")

for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    if i == 9:
        pass
    print(i)

print("~ For Loop ~\n")


# WHILE LOOP
print("~ While Loop ~")

z = 0
while z < 10:
    print(z)
    z += 1

print("~ While Loop ~\n")


# ITERATE THROUGH THE FOR LOOP WITH VARIABLE FOR "INDEX"
print("~ Loop \"In\" ~")

my_list = ['A','B','C']
index_num = 1
for my_element in my_list:
    print(index_num, my_element)
    index_num += 1

print("~ Loop \"In\" ~\n")


# USE THE RANGE FUNCTION ALONG WITH LEN() TO GET THE INDEX NUMBER. USE THAT TO PRINT ELEMENT AND INDEX
print("~ Loop \"Range\" ~")

for index_num in range(len(my_list)):
    my_element = my_list[index_num]
    print(index_num, my_element)

print("~ Loop \"Range\" ~\n")


# ENUMERATE INDEX NUMBER AND ELEMENT FROM LIST EACH LOOP
print("~ Loop Enumerate ~")

for index_num, my_element in enumerate(my_list, start = 1):
    print(index_num, my_element)

print("~ Loop Enumerate ~\n")


# USE INDEX NUMBER TO PRINT DIFFERENT ON LAST LOOP
print("~ Change For Last ~")

hourly_temperature = [90, 92, 94, 95]
for index_num, my_element in enumerate(hourly_temperature):
    if  index_num == len(hourly_temperature) - 1:
        print('%d ' % my_element)
    else: 
        print('%d -> ' % my_element, end='')

print("~ Change For Last ~\n")

