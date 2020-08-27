def is_palindrome(s):
  i = len(s)/2
  for i in range (len(s)//2):
    if s[i] != s[-i-1]: return False
  return True

print(is_palindrome("kajak"))

print(is_palindrome("aa"))

print(is_palindrome("111112"))