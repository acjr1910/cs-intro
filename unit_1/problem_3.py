s = ''  # any lower case string
longest_substring = ''
temp_substring = ''

for i in range(len(s)-1):
    curr_char_int = ord(s[i])
    next_char_int = ord(s[i+1])
    if next_char_int >= curr_char_int:
        temp_substring += s[i]
    else:
        temp_substring += s[i]
        if (len(temp_substring) > len(longest_substring)):
            longest_substring = temp_substring
        temp_substring = ''

if longest_substring == '' and temp_substring != '':
    longest_substring = temp_substring + s[len(s) - 1]

print('Longest substring in alphabetical order is:', longest_substring)
