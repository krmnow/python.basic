def getint():
    while True:
        try:
            number = int(input("Please enetr a number: "))
            return number
        except ValueError:
            print("Invalid number netred, please try again")
            
