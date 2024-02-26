def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    n = [x for x in walk if x == 'n']
    s = [x for x in walk if x == 's']
    e = [x for x in walk if x == 'e']
    w = [x for x in walk if x == 'w']
    if (len(n) == len(s)) and (len(e) == len(w)):
        return True
    else:
        return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))