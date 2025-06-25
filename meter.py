#find how many curtains made from this pieces
pieces=[10,5,40,65,8,9]
cc=0
for i in pieces:
    if i>=9:
       cc += i//9
print(cc)


 