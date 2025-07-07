from operator import truediv


class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other): #operator overloading, updating original add method (for + we are using __add__ method)
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __gt__(self,other): #operator overloading
        m1 =self.m1+self.m2
        m2 =other.m1+other.m2
        if m1 > m2:
            return True
        else:
            return False


s1 = Student(83,28)
s2 = Student(65,59)
s3=s1 + s2
print(s3.m1)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")