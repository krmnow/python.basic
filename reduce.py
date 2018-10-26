import timeit
import functools

def calc_vaues(x, y: int):
    return x+ y

numbers = [2, 3, 5, 8, 13]

reduced_value = functools.reduce(calc_vaues, numbers)
print(reduced_value)
