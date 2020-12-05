#     -14    987654321
      # 01234567890123
parrot="Norwegian Blue"
print(parrot[0:6]) #norweg
print(parrot[3:4 ])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[6: ])
print(type(parrot[6:]))
print(parrot[:6]+parrot[6:])
print(parrot[:])
print(parrot[-4:-5])#no working backward in slicing
print(parrot[-4:2]) #not working backward in slicing
print(parrot[-4:-2])
print(parrot[-4:])
print(parrot[-4:12])
print(parrot[0:6:2])#Nre
print(parrot[0:6:3]) #Nw
number="9,223;372:036 854,775;807"
seperators= number[1::4]
print(seperators)
values="".join(char if char
               not in seperators
               else
               ""
               for char in number).split()
print([int(val) for val in values])

###slicing backwards###
letters ="abcdefghijklmnopqrstuvwxyz"
backwards=letters[25:0:-1] #backward slicing has this rule, stop index must be greater than the start index

print(backwards)
backwards_all=letters[25::-1]
print(backwards_all)
backwards_all_second=letters[::-1]
print(backwards_all)
#challenge
#print qpo
print(letters[16:13:-1])
#print edcba
print(letters[4::-1])
#last characters in reverse order zyxwvuts
print(letters[25:17:-1])
print(letters[-9::-1])
print(letters[:-9:-1])
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])