def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x = int(input("enter a number to calculate its factorial"))
result = factorial(x)
print(result)