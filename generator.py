def topten():
    n=1
    while n <= 10:
        sq = n*n
        yield sq   #yield is used for generator
        n += 1
values=topten()
for i in values:
    print(i)