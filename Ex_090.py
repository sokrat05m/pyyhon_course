url = "http://www.jz634v3en6j.jp/img/m"
sep = ['//', '.']
for i in sep:
    url = ' '.join(url.split(i))
url = url.split()
if 'www' in url:
    url.remove('www')
if 'http:' in url:
    url.remove('http:')
if 'https:' in url:
    url.remove('https:')
print(url)

