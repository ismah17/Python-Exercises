i = 0
while i < 10:
    print(i)
    i += 1
list = ["east", "west", "south", "north"]

expected_input = ""
while expected_input not in list:
    expected_input = input("please select a direction")
    if expected_input.casefold() == "quit":
        print("GAME OVER!")
        break
print("you managed to get out of the loop")
