def getint(prompt):
    while True:
        try:
            number = int(input("Please enetr a number: "))
            return number
        except Exception:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("the finally clause always executed")
            
first_number = getint("please enter first numer")
second_number = getint("please enter second numer")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("You cant divide by zero")  
    sys.exit(2)
else:
    print("Division perfprmed succesfully")
    
