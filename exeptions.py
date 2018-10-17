def factorial(n):
    # n! can also be defined as n = (n-1)
    if n <= 1:
        return 1
    else:
        print(n / 0)
        return n * factorial(n-1)
 
try:    
    print (factorial(1000))
except RecursionError:
    print("This progranm calculate factorial that large")
except ZeroDivisionError:
    print("Nie dziel przez zero")    

print("program terminating")
