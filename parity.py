def main():
    x = int(input("Enter a number: "))
    if parity(x):
        print("x is an even number")
    else:
        print("x is an odd number")

# parity function takes an int and returns a bool
def parity(n):
    if n % 2 == 0:
        return True
    else:
        return False



main()
