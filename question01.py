class point:
    def __init__(self,x,y,z):
        self.x= x
        self.y= y
        self.z= z
        print('values:           ',self.x,'  ',self.y,'  ', self.z)
        
    def squ(self):
        self.x **= 2
        self.y **= 2
        self.z **= 2
        print('squares of values:',self.x,'  ',self.y,'  ',self.z)

    def sum_squ(self):
        data= self.x + self.y + self.z
        print("squares sum of values :",data)
x = float(input('enter x:'))
y = float(input('enter y:'))
z = float(input('enter z:'))
point_obj1 = point(x, y, z)
point_obj1.squ()
point_obj1.sum_squ()