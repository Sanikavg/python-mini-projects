class area:
    a=0
    def __init__(self,length,breadth):
        self.length=float(input("Enter length: "))
        self.breadth=float(input("Enter breadth: "))
        
    def value(self):
        a=self.length*self.breadth
        print(a)
a1=area(56,65)
a1.value()

        


