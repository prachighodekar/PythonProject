class Add():
    s=0
    def sum(self,a= None,b=None,c=None):  #python doesnt support method overloading directly you can use none keyword and can use 2 or 3 or any number of variables in same method
        if a!=None and b!=None and c!=None:
            self.s=a+b+c
        elif a!=None and b!=None:
            self.s=a+b
        else:
            self.s=a
        return self.s
a = Add()
print(a.sum(5,8,9))