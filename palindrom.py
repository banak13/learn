def is_palindrome(s):

  return list(s) == list(s)[::-1]




print(is_palindrome("kajak"))

print(is_palindrome("aa"))

print(is_palindrome("111112"))