class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1")
    def feature2(self):
        print("feature 2")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature3(self):
        print("feature 1")
    def feature4(self):
        print("feature 2")

a1 = B()
#a1.__init__()