def reversesentence(s):
    words = s.split()
    return ' '.join(words[::-1])

print(reversesentence("один два три"))