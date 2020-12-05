name = input("Hi, What is your name?")
if name:
    print("Hello {}! , Enter you age".format(name))
    age = int(input())

    if 18 <= age <= 30:
        print("Welcome to the resort, enjoy your stay!")
    else:
        print("Not allowed")
else:
    print("Enter your name or fuck off....")

