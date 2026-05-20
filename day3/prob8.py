
py = {}
for x in range(1, 100):
    for y in range(x, 100):   
        for z in range(y, 100):
            if z*z == x*x + y*y:
                
                
                py[x , y , z] = sum([x, y, z])

for i in py:
    print(i,py[i])
