a = 3
b = 2
n = 3

if n == 2:
    print(a**2 + 2*a*b + b**2)
elif n == 3:
    print(a**3 + 3*a**2*b + 3*a*b**2 + b**3)
elif n == 4:
    print(a**4 + 4*a**3*b + 6*a**2*b**2 + 4*a*b**3 + b**4)
else:
    print("wrong input")
