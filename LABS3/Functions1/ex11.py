def is_palindrome(s):
    return (s).lower() == (s[::-1]).lower()

print(is_palindrome("madam"))

print(is_palindrome("Madam"))

print(is_palindrome("Madamd"))