class A:
    def Show(self):
        print('A')
class B(A):             #method Show is overriden inside class B after creating object of B
    def Show(self):     #it will first search for show method of itself and if B doesnt have then will execute show method of class A
        print('B')
a1 = B()
a1.Show()
a2 = A()
a2.Show()