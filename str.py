str1 = 'apple'
ch1 = 'a'
ch2 = 'p'
str2 = ' ' 
for i in str1:
    if i == ch1:
        str2 += ch2
    elif i == ch2:
        str2 += ch1
    else:
        str2 +=i
print(str2)             