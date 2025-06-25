List1 = [10,9,8,7,6]
for j in range(len(List1) - 1):
    if List1[j] > List1 [j + 1]:
        List1[j] , List1[j + 1] = List1[j + 1] , List1[j]
print(List1)