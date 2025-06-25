#Reverse String
def reverseString(str1):
    newString =''
    str1 ='hello'
    for i in range(len(str1) -1, -1 , -1):
        newString += str1[i]
print(f'{reverseString(str1)}')




