def squaregenerator(n):
    for x in range(1, n+1):
        yield x ** 2

n = 5
for x in squaregenerator(n):
    print(x)