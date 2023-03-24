n = int(input())
denominator = int(input())
try:
    x = n // denominator
except ZeroDivisionError:
    print("Division by zero is not supported")
else:
    print(x)