List1 = [5,4,3,2,1]
min_index = 0
for i in range (1,len(List1)):
    if List1[i]<List1[min_index]:
        min_index = i
print(List1[min_index])