#print phythogoroeas number
import math
lst = []
for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            if z*z == sum([x*x , y*y]):
                lst.append((x,y,z))
         
print(f"the required list{lst}")