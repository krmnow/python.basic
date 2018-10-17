def factorial(n):
    # n! can also be defined as n = (n-1)
    if n <= 1:
        return 1
    else:
     return n * factorial(n-1)
 
try:    
    print (factorial(10))
except RecursionError:
    print("This progranm calculate factorial that large")
    
print("program terminating")
