answer = 5

print("enter a number between 0 and 10")
guess = int(input())
# if guess > answer:
#   print("guess lower")
#  guess = int(input())
# if guess == answer:
#    print("well done, you guessed it")
# else:
#   print("sorry, you guessed wrong")

# elif guess < answer:
#    print("guess higher")
#   guess = int(input())
#  if guess == answer:
#     print("well done! you guessed it")
# else:
#   print("sorry, you guessed wrong")
# else:
#   print("you guessed it correct, It is 5")

# if guess != answer:
# if guess < answer:
#   print("guess higher")
# else:
#   print("guess lower")
# guess = int(input())
# if guess == answer:
#     print("well done")
#  else:
#       print("sorry, you guessed wrong")
# else:
#  print("well done, you guessed it the first time")

if guess == answer:
    print("well done you guessed it first time")
else:
    if guess > answer:
        print("guess lower")
    else:
        print("guess higher")
    guess = int(input())
    if answer != guess:
        print("sorry, you guessed wrong")
    else:
        print("you guessed correct")

age = int(input("age?"))
if 16 <= age <= 65:
    print("you are grown up")
else:
    print("enjoy while you can")
print("_" * 80)

if age < 16 or age > 65:
    print("enjoy while you can")
else:
    print("have a nice day at work ")
