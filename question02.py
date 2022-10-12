
class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        addition = self.num1 + self.num2
        return addition

    def sub(self):
        subtraction=self.num2 - self.num1
        return subtraction

    def mul(self):
        multiplication= self.num1 * self.num2
        return multiplication

    def div(self):
        division = self.num2 / self.num1
        return division
num1 = float(input("enter num1:"))
num2 = float(input("enter num2:"))
calculator_obj=calculator(num1,num2)
print('addition:' ,calculator_obj.sum())
print('subtraction:',calculator_obj.sub())
print('multiplication:',calculator_obj.mul())
print('division:',calculator_obj.div())
