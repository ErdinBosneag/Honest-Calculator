x = input()
l = []
while True:
    if x == '.':
        break
    else:
        l.append(float(x))
        x = input()
print(min(l))

