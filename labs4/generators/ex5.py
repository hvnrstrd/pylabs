def fromherotozero(n):
    while n >= 0:
        yield n
        n -= 1

n = 5
for x in fromherotozero(n):
    print(x)