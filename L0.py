#round(x, digit to be rounded to)
#split takes two args and can be used in a similar way as other StrOps

#main can be used to organize our code better and keep it understandable without
#having to write the pythonic logical way.
def main():
    #input and function calls listed inside the main function
    name = input("what is your name? ")
    hello(name)
    x = int(input("please enter a number x: "))
    print("The square of x is:", square(x))

#functions defined further down the file for organization of code.
def square(x):
    return x*x

def hello(name):
    print("Hello, " + name)


#calling main function which allows us to actually execute the processes inside of main
main()