d = { "me" : [200,300], "you": [400,1,3]}
c = type(d)
print(c)
for i in d:
    v = len(d[i])
    print(v)
    
    
for i in d:
    if i == "me":
        d[i].extend([20,30])
        
print(d)         
for i in d:
    sum = 0
    for k in d[i]:
        sum += k
            
    print("the sum of each value:",sum)  
    sum += len(d)
    print("the sum of each value after adding key length:",sum)
    


        
 
  
   
   
   
    
