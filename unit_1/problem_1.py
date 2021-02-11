s = ''  # any lower case string
vowelsCount = 0

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowelsCount += 1

print(vowelsCount)
