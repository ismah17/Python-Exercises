name = input("enter name")
age = int(input("how old are you {}".format(name)))
print(age)

if age >= 18:
    print("you are old enough to vote")
elif age == 900:
    print('sorry, Yoda, you die in return of Jedi')
else:
    print("please come back in {} years". format(18-age))
