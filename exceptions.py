#exceptions are the errors that might occur in python.


# print("hello, world) - unterminated string
#   syntax errors


#ValueError
#try and except
#sort of like an if-else for the whole code.

try:
    #do this if correct
    n = int(input("What's n?"))
    print(f"n is {n}")
except ValueError:
    #otherwise do this in the case of this error
    print("n is not an integer")


#NameError resolved

try:
    n = int(input("What's n?"))
except ValueError:
    print("n is not an integer")
else:
    print(f"n is {n}")