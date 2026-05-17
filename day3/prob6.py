D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
t = D1 | D2
print(t)
m = {} 
for i in D1:
    for j in D2:
        if i == j:
            v = D1[i] + D2[j]
            m[i] = v
       

for k in D1:
    if k not in m:
        m[k] = D1[k]
        
    
for l in D2:
    if l not in m:
        m[l] = D2[l]
        
print(m)
