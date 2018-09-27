
def fact(n):
    #calclulate n! literatively """"
    result = 1
    if n > 1:
        for i in range(2, n + 1):
            result *= n
        return result

for i in range(130):
    print(i, fact(i))
