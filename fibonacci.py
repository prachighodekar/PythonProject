
def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<1:
        print("enter positive integer")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
number = int(input("enter a number"))
fib(number)
