s = {1,2,3}
if s == {3,2,1}:
    print("same")
else:
    print("no - same")
    
if 30 not in s:
    print("not-part")


    
o = list(s)
print(o)   
print(o[0])
r = set()
for i in s:
    x = i+10
    r.add(x)

print(r)


