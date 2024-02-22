def evennumbersbetween0andn(n):
    for x in range(n + 1):
        if x % 2 == 0:
            yield x

n = 10
for x in evennumbersbetween0andn(n):
    print(x)