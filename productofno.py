num = 567
numProduct = 1
while num != 0:
    rem = num%10
    numProduct = numProduct*rem
    num //= 10
print(numProduct)