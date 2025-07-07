from functools import reduce

nums = [2,8,5,4,7,9,3,1,5,2]
even = list(filter(lambda n: n % 2 == 0, nums))
print(even)
doubles = list(map(lambda n : n*2, even))
print(doubles)
sum = reduce(lambda a,b: a+b, doubles)
print(sum)