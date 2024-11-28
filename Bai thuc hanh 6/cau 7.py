print("Nguyen Van Thai","\nMSSV: 235752021610005")
class Circle:
    def __init__(self,r):
        self.r=r

    def cv(self):
        return self.r*2*3.14

    def dt(self):
        return self.r**2*3.14
a=Circle(5)
print('Chu vi hinh tron la: ',a.cv(),'\nDien tich hinh tron la: ',a.dt())

    
