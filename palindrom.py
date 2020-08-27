def is_palindrome(palindrom):
    palindrom = list(palindrom.replace(" ", "").lower())
    return palindrom == list(reversed(palindrom))





print(is_palindrome("Zakopane na pokaz"))

print(is_palindrome("Aa"))

print(is_palindrome("111112"))