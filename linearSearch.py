from operator import truediv

pos = -1
def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False


list = [1,4,7,0,3,4,5]
n = int(input("Enter a number: "))
if search(list,n):
    print("found at ", pos+1)
else:
    print("not found")