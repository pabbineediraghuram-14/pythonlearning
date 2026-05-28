
D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

DU = {}
for i in D1:
    DU[i] = D1[i]

    
for j in D2:
    DU[j] = D2[j]
    
print(DU)
DI = {}
for i in D1:
    if i in D2:
        DI[i] = D1[i]
        
        
print(DI)
DS = {}
for i in D1:
    if i not in D2:
        DS[i] = D1[i]
        
print(DS)        