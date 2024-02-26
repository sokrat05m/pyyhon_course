romans = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
    }
s = 'III'
i = len(s) - 2
result = romans[s[-1]]
while i >= 0:
    if romans[s[i]] < romans[s[i+1]]:
        result -= romans[s[i]]
    else:
        result += romans[s[i]]
    i -= 1
print(result)


