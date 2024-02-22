def squares(a, b):
    for x in range(a, b + 1):
        yield x ** 2

a, b = 1, 5
for x in squares(a, b):
    print(x)