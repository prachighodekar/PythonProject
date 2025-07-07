class Pycharm():
    def execute(self):
        print("Compile")
        print("execute")
class MyEditor():
    def execute(self):
        print("spell check")
        print("Compile")
        print("execute")

class Laptop():
    def code(self,ide):
        ide.execute()
        
ide = MyEditor()
a1 = Laptop()
a1.code(ide)