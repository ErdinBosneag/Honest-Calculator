string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
n = 0
for vowel in vowels:
    for char in string:
        if vowel == char:
            n += 1
print(n)


