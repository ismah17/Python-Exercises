"""print numbers from 0 to 20 that are not divisible by 3 or 5"""
list1 = []
list2 = []
for number in range(0, 20, 3):
    if number == 0:
        continue
    else:
        list1.append(number)

for i in range(0, 20, 5):
    if i == 0:
        continue
    else:
        list2.append(i)

list = list1 + list2
non_divisible =[]

for num in range(0, 20):
    if num in list or num ==0:
        continue
    else:
        non_divisible.append(num)
print(non_divisible)

