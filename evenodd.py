

def EvenOdd(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd
lst = [5,6,8,3,2,1]
even,odd = EvenOdd(lst)
print("even : {} odd : {}".format(even,odd))
