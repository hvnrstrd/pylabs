def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if (2 * chickens) + (4 * rabbits) == num_legs:
            return chickens, rabbits
    return None, None

heads = int(input("number of heads: "))
legs = int(input("number of legs: "))
chickens, rabbits = solve(heads, legs)

if chickens is None:
    print("no proper solution")
else:
    print(f"chickens: {chickens}, rabbits: {rabbits}")
