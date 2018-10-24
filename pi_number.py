def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2

def pi_servies():
    odds = oddnumbers()
    appro = 0
    while True:
        appro += (4 / next(odds))
        yield appro
        appro -= (4 / next(odds))
        yield appro
        
aprox_pi = pi_servies()

for x in range(10000):
    print(next(aprox_pi))
