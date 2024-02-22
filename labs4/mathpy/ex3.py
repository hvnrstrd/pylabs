import math
print(f"Area: {(lambda n, s: (n * s**2)/(4 * math.tan(math.pi / n)))(int(input('Sides: ')), int(input('Side length: ')))}")