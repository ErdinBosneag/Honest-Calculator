def is_one_digit(v):
    if type(v) == float:
        if (10 > v > -10) and v.is_integer():
            output = True
        else:
            output = False
    elif type(v) == int:
        if (10 > v > -10):
            output = True
        else:
            output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += " ... very, very lazy"
    if msg != '':
        msg = "You are" + msg
        print(msg)


num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "M"]
operations = ["+", "-", "*", "/"]
j = 0
memory = 0
while j != 1:
    x, oper, y = input("Enter an equation ").split()
    b = 1
    k = 0
    for i in x:
        if i in num:
            if i == '.':
                k = 1
        else:
            print("Do you even know what numbers are? Stay focused!")
            b = 0
            break
    if b != 0:
        if k == 1:
            x = float(x)
        elif x == 'M':
            x = memory
        else:
            x = int(x)
        k = 0
        a = 1
        for i in y:
            if i in num:
                if i == '.':
                    k = 1
            else:
                print("Do you even know what numbers are? Stay focused!")
                a = 0
                break
        if a != 0:
            if k == 1:
                y = float(y)
            elif y == 'M':
                y = memory
            else:
                y = int(y)
            c = 1
            if oper not in operations:
                print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
                c = 0
            if c != 0:
                check(x, y, oper)
                f = 1
                if oper == '+':
                    result = x + y
                elif oper == '-':
                    result = x - y
                elif oper == '*':
                    result = x * y
                elif oper == "/":
                    if y != 0:
                        result = x/y
                    else:
                        print("Yeah... division by zero. Smart move...")
                        f = 0
                if f != 0:
                    print(float(result))
                    j = 1
                    p = 0
                    while p != 1:
                        answer = input("Do you want to store the result? (y / n):")
                        if answer == 'y':
                            v = 1
                            msg_index = 10
                            if is_one_digit(result):
                                z = 1
                            else:
                                z = 0
                            while z != 0:
                                if msg_index == 10:
                                    msg = "Are you sure? It is only one digit! (y / n)"
                                elif msg_index == 11:
                                    msg = "Don't be silly! It's just one number! Add to the memory? (y / n)"
                                else:
                                    msg = "Last chance! Do you really want to embarrass yourself? (y / n)"
                                ans = input(msg)
                                if ans == "y":
                                    if msg_index < 12:
                                        msg_index += 1
                                    else:
                                        z = 0
                                        break
                                else:
                                    z = 0
                                    v = 0
                                    break
                            if v == 1:
                                memory = result
                            u = 0
                            while u != 1:
                                answer2 = input("Do you want to continue calculations? (y / n):")
                                p = 1
                                if answer2 == 'y':
                                    j = 0
                                    u = 1
                                elif answer2 == 'n':
                                    u = 1
                                    continue
                                else:
                                    continue
                        elif answer == 'n':
                            u = 0
                            while u != 1:
                                answer2 = input("Do you want to continue calculations? (y / n):")
                                p = 1
                                if answer2 == 'y':
                                    j = 0
                                    u = 1
                                elif answer2 == 'n':
                                    u = 1
                                    continue
                                else:
                                    continue
                        else:
                            continue
