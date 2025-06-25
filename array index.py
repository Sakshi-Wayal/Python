L1 = [5,4,3,2,1]
min_index = 0
for i in range( 0 + 1, len(L1)):
    if L1[i] < L1[min_index]:
        min_index=i
L1[0], L1[min_index] = L1[min_index], L1[0] 
print(L1)