
try:
    val=10/0
    number = int(input("enter a number"))
    print(number)
except ZeroDivisionError as Err:
    #print("divided by zero")
    print(Err)
except ValueError:
    print("invalid input")
