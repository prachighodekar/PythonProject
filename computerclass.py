class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is",self.cpu,self.ram)

com = computer("amd",16)
com.config()