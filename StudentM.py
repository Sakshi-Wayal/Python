#find the student marks greater then 35
#find lowest marks
#find highest marks
Marks = [10,35,40,65,75,90,21,34,82,17]
count =0
high=Marks[0]
low=Marks[0]
for i in Marks:
    if(i>=35):
       count +=1
print(count)
for i in Marks:
    if i>high:
        high=i
print(high)
for i in Marks:
    if i<low:
        low=i
print(low)




