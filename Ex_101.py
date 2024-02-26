def is_sub(st, tr):
    index = 0
    for i in st:
        try:
            index = tr.index(i, index)
        except ValueError:
            return False
        index += 1

    return True


s = 'aaaaaa'
t = 'bbaaaa'
print(is_sub(s, t))



