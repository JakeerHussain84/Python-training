class methodoverride1:
    def display(self):
        print("method involved from base class")
class methodoverride2(methodoverride1):
    def display(self):
        print("method involved from derived class") 
ob=methodoverride2()
ob.display()
    
    