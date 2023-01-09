import sys

try:
    # try block
    print(sys.argv[1])
except Exception as e:
    # handle specific exceptions and then all others
    print(f"ERROR: {e}")
else:
    # will run if try block has no exceptions
    print("Valid User Input")
finally:
# runs no matter what even if exceptions are raised in try block
    print("Always Runs")
