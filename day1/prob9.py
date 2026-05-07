import math
u = float(input("enter the intial velocity"))
a = float(input("enter the intial acceleration"))
t = float(input("enter the time"))
s = float(input("enter the displacement"))
v = u + a*t #final velocity using u,a,t.
print("the final velocity using u,a,t",v)
v = math.sqrt(u*u + 2*a*s) # using u,s,a.
print("the final velocity using u,s,a",v)
s = u*t + 0.5*a*t*t #using u,t,a.
print("the diaplcement",s)