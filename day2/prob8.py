#print phythogoroeas number
lst = []
for x in range(1,100):
    for y in range(x,100):
        for z in range(y,100):
            if z*z == x*x + y*y:
                lst.append((x,y,z))
         
print(lst)