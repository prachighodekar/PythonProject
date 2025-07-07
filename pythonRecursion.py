
def factorialRecursion(n):
    if n==0:
        return 1
    return n*factorialRecursion(n-1)

result = factorialRecursion(3)
print(result)