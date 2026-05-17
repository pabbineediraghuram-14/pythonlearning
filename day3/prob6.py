D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
print(D1 | D2)
m = {} 
for i in D1:
    for j in D2:
        if i == j:
            v = D1[i] + D2[j]
            m[i] = v
        if i not in m:
            m[i] = D1[i]
        if j not in m:
            m[j] = D2[j]
        
print(m)
