###string formatting###

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))

###string formatting###
print("left aligned and ")
for i in range(1, 13):
    print("No. {0} squared is {1:<3} and cubed is {2:^5}".format(i, i**2, i**3))

print()

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7)) #floating point has 6 digits of precision
print("Pi is approximately {0:12.50f}".format(22/7)) #can't fit a precision of 50 in a 12 field width, python decided precision is more important
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7)) #field width is 72 and precision is 50
print("Pi is approximately {0:<72.54f}".format(22/7))
print("Pi is approximately {0:<72.50f}".format(22/7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))


print()
for i in range(1, 13):
    print("No. {} squared is {:^4} and cubed is {:^5}".format(i, i**2, i**3))