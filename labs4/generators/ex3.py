def divisibleby3and4(n):
    for x in range(1, n + 1):
        if x % 3 == 0 and x % 4 == 0:
            yield x

n = 10
for x in divisibleby3and4(n):
    print(x)