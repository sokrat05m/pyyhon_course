s = 'key1:value1:key2:value2:key3::key4:value4'
list_1 = s.split(':')
d = {}
i = 0
while i < len(list_1):
    d[list_1[i]] = list_1[i + 1]
    i += 2
s2 = ''
for k, v in d.items():
    s2 += k + ':' + v + ':'
print(s2[:-1])

