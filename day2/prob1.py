pit = [1,2,3,5,6]
print("number of elements:",len(pit))
if 7 in pit:
    print("7 is in the list")
else:
    print("7 is not in the list")
    
if pit == [1, 2, 3]:
    print("same")
else:
    print("Not same")
    
    
pit[0] = pit[0] + 10
print(pit)
