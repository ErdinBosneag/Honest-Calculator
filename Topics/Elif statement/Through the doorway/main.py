A = int(input())
B = int(input())
C = int(input())
X = int(input())
Y = int(input())
if A > X:
    if B > X or C > X:
        print("The box cannot be carried")
    else:
        print("The box can be carried")
elif B > X:
    if A > X or C > X:
        print("The box cannot be carried")
    else:
        print("The box can be carried")
elif C > X:
    if A > X or B > X:
        print("The box cannot be carried")
    else:
        print("The box can be carried")
else:
    print("The box can be carried")





