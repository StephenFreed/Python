"""
Whenever we run a Python application, we are provided a built-in namespace that 
is created when the interpreter is started and has a lifetime until the interpreter 
terminates (usually when our program is finished running). Since Python provides the 
namespace, these objects are accessible without the need to import a separate module.
"""

print("~~~~~~~~~~~~~~ builtins ~~~~~~~~~~~~~~")
print(dir(__builtins__))
print("~~~~~~~~~~~~~~ builtins ~~~~~~~~~~~~~~")


"""
The global namespace exists one level below the built-in namespace. Generally, 
it includes all non-nested names in the module (file) we are choosing to run the 
Python interpreter on. The global namespace is created when we run our main program 
and has a lifetime until the interpreter terminates (usually when our program is finished running).
"""

"""
the global namespace contains all of the non-nested objects of our program

anytime we use the import statement to bring in a new module into our program, 
instead of adding every name from that module (such as all the names in the random module) 
to our current global namespace, Python will create a new namespace for it. 
This means there might be potentially multiple global namespaces in a single program.
"""

print("~~~~~~~~~~~~~~ Globals ~~~~~~~~~~~~~~")
my_global_var = "Global"
print(globals())

import sys
print(globals())

global_variable = "global"
def print_global():
  global_variable = "nested global"
  nested_variable = "nested value"
  print("~~~~~~~~~~~~~~ Locals ~~~~~~~~~~~~~~")
  print(locals())
  print("~~~~~~~~~~~~~~ Locals ~~~~~~~~~~~~~~")

print(globals())
print("~~~~~~~~~~~~~~ Globals ~~~~~~~~~~~~~~")

print_global()
