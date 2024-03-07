def counter(strs):
    ucase, lcase = 0, 0
    for x in strs:
        if x.isupper():
            ucase += 1
        elif x.islower():
            lcase += 1
    return ucase, lcase
str1 = "AaaaAAAa help me i stucked in string"
uppercase, lowercase = counter(str1)
print(f'upper case: {uppercase},lower case: {lowercase}')
