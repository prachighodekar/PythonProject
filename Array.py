from array import *

n = array('i', [])
num = int(input("Enter the size of the array "))

for i in range(num):
    x = int(input("Enter the number "))
    n.append(x)

print(n)
k=0
search = int(input("Enter the number to search "))
found = False
for e in n:
    if e == search:
        print("The index of", search, "is", k)
        break
    k+=1
if not found:
    print(search, "is not in the array")

#print(n.index(search))