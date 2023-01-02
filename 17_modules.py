#pip
# A module is a collection of Python declarations intended broadly to be used as a tool. 
# Modules are also often referred to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.
#
# Usually, to use a module in a file, the basic syntax you need at the top of that file is:
#
# from module_name import object_name

import random
import time

# Create random_list of 100 numbers.
random_list = []
for i in range(101):
  random_list.append(random.randint(1,100))
print(len(random_list))

# Create randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)

localtime = time.asctime( time.localtime(time.time()) )
print( "Local current time is:", localtime )

import datetime
print(datetime.date.today())
