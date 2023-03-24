number = int(input())
_units = number % 10
_decimals = number // 10 % 10
_hundreds = number // 100
print(_units + _decimals + _hundreds)
