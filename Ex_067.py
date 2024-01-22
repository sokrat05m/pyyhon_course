def is_pangram(s):
    check = 'qwertyuiopasdfghjklzxcvbnm'
    lst = []
    for i in check:
        if i in s.lower():
            lst.append(0)
        else:
            lst.append(1)
    if 1 in set(lst):
        return False
    else:
        return True


a = is_pangram('The quick brown fox jumps over the lazy dog')
print(a)