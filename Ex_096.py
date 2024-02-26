rans = 'fihjjjjei'
magazine = 'hjibagacbhadfaefdjaeaebgi'
rans_hash = {}
mag_hash = {}
for i in rans:
    if i not in rans_hash:
        rans_hash[i] = 1
    else:
        rans_hash[i] += 1
for i in magazine:
    if i not in mag_hash:
        mag_hash[i] = 1
    else:
        mag_hash[i] += 1

for i in rans:
    if i not in mag_hash:
        print('false')
    elif rans_hash[i] > mag_hash[i]:
        print('false')
    else:
        print('true')

print(rans_hash)
print(mag_hash)