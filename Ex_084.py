def to_camel_case(text):
    res = ''
    i = 0
    while i < len(text):
        if text[i] == '_' or text[i] == '-':
            res += text[i+1].upper()
            i += 2
        else:
            res += text[i]
            i += 1
    return res


print(to_camel_case('camel_case'))
