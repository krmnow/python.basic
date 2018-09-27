def fact(n):
    #calclulate n! literatively """"
    result = 1
    if n > 1:
        for i in range(2, n + 1):
            result *= n
        return result

def factorial(n):
    # n! can also be defined as n *(n-1)
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(36):
    print(i, factorial(i))
