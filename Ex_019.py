text = input("Input text: ").lower()
separator = "!,.?@:;"
for i in separator:
    text = ''.join(text.split(i))
print(text)
print(len(set(text.split())))