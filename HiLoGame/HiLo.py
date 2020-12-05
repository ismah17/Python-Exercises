
low = 1
high = 1000
print("please think of a number between {} and {} ".format(low, high))
input("press ENTER to start")
guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. should I guess high or low?"
                     "enter h or l, or c if my guess is correct"
                     .format(guess)).casefold()
    if high_low == "h":
        #guess higher,the lower end becomes 1 greater than the guess

        low = guess +1
    elif high_low == "l":
        #guess lower, the high end of the range becomes one less than guess
        high = guess -1
    elif high_low =="c":
        print("i got it in {} guesses".format(guesses))
        break
    else:
        print("enter h, c or l")
    guesses = guesses +1


