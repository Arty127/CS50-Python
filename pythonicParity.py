def main():
    x = int(input("Enter a number: "))
    if parity(x):
        print("x is an even number")
    else:
        print("x is an odd number")
#the pythonic way of coding like human language.
# parity function takes an int and returns a bool
#def parity(n):
    #return True if n%2 == 0 else False

def parity(n):
    return n%2 == 0

main()





def parity(n):
    return n%2 == 0