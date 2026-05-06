import math
u = 5 #intial velocity
a = 7 # accleration
t = 6 #time
s = 10 # displacement
v = u + a*t #final velocity using u,a,t.
print(v)
v = math.sqrt(u*u + 2*a*s) # using u,s,a.
print(v)
s = u*t + 0.5*a*t*t #using u,t,a.
print(s)