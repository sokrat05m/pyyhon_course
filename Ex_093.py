s = "`l;`` 1o1 ??;l`"
s = s.lower()
separator = '''|!',`.?@:; #_/}{)("[]-'''
for i in separator:
    s = ''.join(s.split(i))
print(s)
res = ''
for i in range(len(s) - 1, -1, -1):
    res += s[i]
print(res)



