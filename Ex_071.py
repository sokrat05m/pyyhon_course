check = 'abcdefghijklmnopqrstuvwxyz'
check1 = check.upper()
text = 'Codewars1'
print(text.find('e'))
res = ''
for i in text:
    if i in check:
        res += check[check.find(i) - 13]
    elif i in check1:
        res += check1[check1.find(i) - 13]
    else:
        res += i

print(res)


