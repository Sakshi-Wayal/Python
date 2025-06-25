n = (int(input('Enter the number')))
oddTotal = 0
for i in range (0,n+1):
    if i%2 != 0:
        oddTotal += i
print(oddTotal)
