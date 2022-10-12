class student:
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_rollno(self,rollno):
        self.__rollno = rollno
    def get_rollno(self):
        return self.__rollno
name = input("enter name:")
rollno=input("enter rollno:")

obj = student()
obj.set_name(name)
print(obj.get_name())

obj.set_rollno(rollno)
print(obj.get_rollno())