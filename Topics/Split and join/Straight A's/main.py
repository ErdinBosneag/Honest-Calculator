# put your python code here
grades = input()
l = grades.split()
n = 0
m = 0
for char in l:
    if char == 'A':
        n += 1
    m += 1
print(round(float(n) / float(m),2))
