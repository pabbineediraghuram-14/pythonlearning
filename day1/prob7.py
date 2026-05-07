import math
a = float(input("enter the 1st number"))
b = float(input("enter the 2nd number "))
ch = input("enter the operation +,-,*,/,sqrt,tan,cos,sin,exp")
if ch == "+":
	c = a + b
	print(c)
elif ch == "-":
	c = a - b
	print(c)
elif ch == "*":
	c = a*b
	print(c)
elif ch == "/":
	c = a/b
	print(c)
elif ch == "sqrt":
	c = math.sqrt(a)
	d = math.sqrt(b)
	print(c,d)
elif ch == "tan":
	c = math.tan(a)
	d = math.tan(b)
	print(c,d)
elif ch == "log":
	c = math.log(a)
	d = math.log(b)
	print(c,d)
elif ch == "sin":
	c = math.sin(a)
	d = math.sin(b)
	print(c,d)
elif ch == "cos":
	c = math.cos(a)
	d = math.cos(b)
	print(c,d)
elif ch == "exp":
	c = math.exp(a)
	d = math.exp(b)
	print(c,d)
else:
    print("invalid operator")