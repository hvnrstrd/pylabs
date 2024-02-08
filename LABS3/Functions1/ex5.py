def print_permutations(s, x=0):

    if x == len(s):
        print("".join(s))

    for i in range(x, len(s)):
        strout = [character for character in s]
        strout[x], strout[i] = strout[i], strout[x]
        print_permutations(strout, x + 1)

print_permutations("ЖДВОКЗАЛ")