def domain_name(url):
    sep = ['//', '.']
    for i in sep:
        url = ' '.join(url.split(i))