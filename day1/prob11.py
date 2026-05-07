#11(1) question
import random

score = 0
for i in range(10):
    user = int(input("enter the number "))
    code = random.randint(1,101)
    if user < code:
        score_user = -1
        score += score_user
    elif user == code:
        score_user = 3
        score += score_user
    elif user > code:
        score_user = 1
        score += score_user
        
print(score)    
if score > 0:
    print("User wins")
elif score < 0:
    print("Code wins")

   
    

