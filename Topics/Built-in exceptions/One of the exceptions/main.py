x = int(input())
n = 0
for char in dir(locals()['__builtins__']):
    if(n == x):
        print(char)
        break
    n += 1