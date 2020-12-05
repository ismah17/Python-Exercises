import random
answer = random.randint(1, 10)
print("guess between 1 and 10")
guess = int(input())
if guess == answer:
    print("you got it right first time")
else:
    if guess < answer:
        print("guess higher")
    else:
        print("guess lower")
    guess= int(input())
    if guess == answer:
        print("well done")
    else:
        print("sorry, wrong answer")
