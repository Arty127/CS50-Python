def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

    #def get_int():
        # build this complete thing first
        # and then put it in the function
    #    while True:
    #        try:
    #            x = int(input("what's x? "))
    #        except ValueError:
    #            print("x is not an integer")
    #        else:
    #            return x

#the other way of doing the same thing in fewer lines
#reusable as any variable can be used by the user
#instead of just x


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #pass - keyword
            pass

main()