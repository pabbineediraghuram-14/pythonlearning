lst = ["OK", "NOK", "hello", "hi"]
e , o , t = 0 , 0 , 0
for i in lst:
    c = len(i)
    if c % 2 == 0:
        e += 1
    else:
        o +=1
    
   
for i in lst:
    c = len(i)
    t += c
    
 
        
print("the total even length strings:",e)
print("the total odd length strings:",o)
print("the total length of all strings:",t)

 
