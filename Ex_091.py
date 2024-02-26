def format_duration(seconds):
    years = seconds // 31536000
    days = (seconds - years * 31536000) // 86400
    hours = (seconds - years * 31536000 - days * 86400) // 3600
    minutes = (seconds - years * 31536000 - days * 86400 - hours * 3600) // 60
    seconds = seconds - years * 31536000 - days * 86400 - hours * 3600 - minutes * 60
    if years > 1:
        y = f'{years} years'
    elif years == 1:
        y = f'{years} year'
    if days > 1:
        d = f'{days} days'
    elif days == 1:
        d = f'{days} day'
    if hours > 1:
        y = f'{hours} hours'
    elif hours == 1:
        y = f'{hours} hour'
    if minutes > 1:
        y = f'{minutes} minutes'
    elif hours == 1:
        y = f'{hours} hour'
    if hours > 1:
        y = f'{hours} hours'
    elif hours == 1:
        y = f'{hours} hour'
