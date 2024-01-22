s1 = 'katas'
s2 = 'steak'
lst = []
for i in range(len(s2)):
    if s2[i] in s1:
        lst.append(0)
        s1 = s1.replace(s2[i], '', 1)
    else:
        lst.append(1)
print(lst)
if len(set(lst)) in (0, 1):
    print(True)

print(s1)


