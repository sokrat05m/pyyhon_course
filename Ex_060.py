s1 = 'javascript'
s2 = 'script'
check = list(s1)
print(check)
for i in s2:
    if i in s1:
        check.remove(i)
    else:
        print('false')
print(check)



