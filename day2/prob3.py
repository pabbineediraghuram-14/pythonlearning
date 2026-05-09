import random
c = []
for i in range(1,11):
    a = random.randint(10,51)
    c.append(a)
    
print(c)
sum = 0
for i in c:
    sum += i
  
print("the sum of elements in the list:",sum)
    