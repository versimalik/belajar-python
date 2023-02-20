class Calculator:
	def __init__(self,a,b,c):
		self.operator = a
		self.num1 = int(b)
		self.num2 = int(c)

	def operate(self):
		if self.operator == "+":
			return self.addition(self.num1, self.num2)
		if self.operator == "-":
			return self.substraction(self.num1, self.num2)
		if self.operator == "*":
			return self.multiplication(self.num1, self.num2)

	def addition(self,num1,num2):
		result = num1 + num2
		print(f"{num1} + {num2} = {result}")

	def substraction(self,num1,num2):
		result = num1 - num2
		print(f"{num1} - {num2} = {result}")

myCalculator = Calculator("-",1,2)
myCalculator.operate()
