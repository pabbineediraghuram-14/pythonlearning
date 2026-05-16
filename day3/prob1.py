d = { "me" : 200, "you": 400}
print(d["you"])
d["ram"] = 800
print(d)
d["ram"] = 900
print(d)
print(len(d))
if "someone" in d:
    print("present")
else:
    print("not present")
    
    
    
print(d.keys())
for i in d:
    d[i] +=100
    
print(d)
    
