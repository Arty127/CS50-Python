def main():
    print_column(45)
    print_row(4)



def print_row(width):
    print('?'*width)

def print_column(height):
    print("#\n"*height, end = " ")




main()