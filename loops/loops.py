numbers = "5,233;345:567 765, 567;788"
separators = ""
for char in numbers:
    if not char.isnumeric():
        separators = separators + char
        print(separators)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)

for i in range(0, 6):
    print("i is now {}".format(i))

for i in range(0, 10, 2):  # 10 is not included in the range
    print(i)

for i in range(12, 10, -2):
    print(i)
for i in range(0, 100):
    if i % 7 == 0:
        print(i)

for i in range(0, 100, 7):
    print("{} is devisible by 7".format(i))

for i in range(100)[::7]:
    print(i)

for i in range(1, 13):
    for j in range(1, 13):
        print("i is {0} and j is {1}".format(i, j))
print(":::::::")

shopping_list = ["milk", "Butter", "Coconut", "Spam"]

for item in shopping_list:  # type: str
    # print("Buy " + item)
    # if item != "Spam":
    #    print("buy " + item)
    if item == "Spam":
        continue
    print("Buy " + item)
i is {0} and j is {}

_list = ["milk", "Orange", "Spam", "rice", "carrot"]
found_at = None
# for index in range(len(_list)):
#   if _list[index] == "Spam":
#       found_at = index
# print("found at {0}".format(found_at))

for index in range(len(_list)):
    if _list[index] == "Spam":
        found_at = index
        break
print("found at {0}".format(found_at))
