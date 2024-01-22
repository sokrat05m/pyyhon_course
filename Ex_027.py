def isIsogram(string):
    list_1 = list(string.lower())
    set_1 = set(list_1)
    if len(set_1) == len(list_1):
        return True
    else:
        return False

b = isIsogram("Dermatoglyphics")
print(b)