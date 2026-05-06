def main():
    name = input("what is your name?")

    #matches and cases can be used in the place of if-else statements.
    #and a seperate case with an "_" can be used in the place of an else statement.
    # "|" can be used to as an alternative to and or keywords


    match name:
        case "Alcina":
            print("Corsetti")
        case "Jordan":
            print("Acosta")
        case "Sadia":
            print("Malik")
        case _:
            print("Who?")
main()
