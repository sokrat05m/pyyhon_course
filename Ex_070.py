def make_readable(seconds):
    res = ''
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = (seconds - hours * 3600 - minutes * 60)
    if hours < 10:
        res += f'0{hours}'
    else:
        res += f'{hours}'
    if minutes < 10:
        res += f':0{minutes}'
    else:
        res += f':{minutes}'
    if seconds < 10:
        res += f':0{seconds}'
    else:
        res += f':{seconds}'
    return res


a = make_readable(3700)
print(a)