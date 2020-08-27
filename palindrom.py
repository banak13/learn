def is_palindrome(s):
    s = list(s.replace(" ", "").lower())
    return s == list(reversed(s))





print(is_palindrome("Zakopane na pokaz"))

print(is_palindrome("Aa"))

print(is_palindrome("111112"))