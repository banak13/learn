def is_palindrome(s):
  i = len(s)/2
  while i:
    i -= 1
    if s[i] != s[-i-1]: return False
  return True



