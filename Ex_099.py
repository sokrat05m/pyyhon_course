s = "rat"
t = "car"
s_hash = {}
t_hash = {}
for i in s:
    if i in s_hash:
        s_hash[i] += 1
    else:
        s_hash[i] = 1
for i in t:
    if i in t_hash:
        t_hash[i] += 1
    else:
        t_hash[i] = 1
for i in s:
    if i not in t_hash:
        print('f')
    elif s_hash[i] != t_hash[i]:
        print('bad')
    else:
        print('good')