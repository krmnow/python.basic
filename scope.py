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

def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minu1 = 1
        n_minu2 = 0
        for f in range(1, n + 1):
            result = n_minu2 + n_minu1
            n_minu2 = n_minu1
            n_minu1 = result
        return result

for i in range(36):
    print(i, fibonacci(i))
