input = "[1,2,3,4]"
#convert this to list of numbers , ouput = [1,2,3,4]
 
#hint - remove [], prefix and suffix from input, then split by , 
#then iterate and convert each string to int by using int()
#and then append to empty list 
o = input[1:-1:1]
y = input[1:-1:1].split(",")
r = []
for u in y:
    t = int(u)
    r.append(t)
    
print(r)
