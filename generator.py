import sys

def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1
#big_range = range(10000)
big_range = my_range(1000)
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []

for val in big_range:
    big_list.append(val)
    
print("big_list is {} bytes".format(sys.getsizeof(big_list)))
