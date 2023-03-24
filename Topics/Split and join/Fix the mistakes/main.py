text = input()
words = text.split()
for word in words:
    c = word.lower()
    if c.startswith("www."):
        print(word)
    elif c.startswith("https://"):
        print(word)
    elif c.startswith("http://"):
        print(word)