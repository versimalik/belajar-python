number1 = int(input("Masukkan angka ke 1: "))
number2 = int(input("Masukkan angka ke 2: "))

def addition(a,b):
	global result # set local to global
	result = a + b
	print(f"{a} + {b} = {result}")

addition(number1,number2)
print(result) # access global variable