# 9. Palindrome Number
def isPalindrome (x):
    y = 0
    a = x
    if x < 0:
        return False
    while x > 0:
        y = y * 10 + x % 10
        x //= 10
    if a == y:
        return True
    return False


c = isPalindrome(121)
print(c)