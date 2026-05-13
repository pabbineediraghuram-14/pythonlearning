import random

scores = []
for i in range(1, 11):
    uin = int(input("enter the number"))
    cn = random.randint(1, 99)

    if uin < cn:
        score = -1
    elif uin == cn:
        score = 3
    else:
        score = 1

    scores.append(score)

    
total = sum(scores)

print("Final Score:",score)


if total > 0:
    print("User Wins!")
elif total < 0:
    print("Code Wins!")

