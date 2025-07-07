

def lessthanfive(lst):
    less_than_five = []
    for i in lst:
        if i < 5:
            less_than_five.append(i)
    return less_than_five

lst = [5,6,8,3,2,1]
result = lessthanfive(lst)
print("the numbers less than 5 are :",result)
print("the count is :",len(result))