def main():
    print_square(12)


#square printing function
def print_square(size):

    #for each row in square
    for i in range(size):

        #for brick in row
        for k in range(size):
            #print brick

            print("#", end='')
        print()
main()