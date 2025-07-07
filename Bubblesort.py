

def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j]=list[j+1]
                list[j+1]=temp



user_input = input("Enter numbers separated by spaces: ")
lst = list(map(int, user_input.split()))
bubble_sort(lst)
print(lst)