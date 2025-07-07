def div(a,b):
    print(a/b)


def samrtdiv(func):
    def innerfun(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return innerfun

div = samrtdiv(div)
div(3,6)