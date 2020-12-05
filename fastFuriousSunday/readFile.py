Employee_file = open("employee.txt", "r")
# options r+ for read and write
# w for write and a fop appending things BUT
# CAN NOT CHANGE THINGS WROTE PREVIOUSLY
#print(Employee_file.readable())
#before reading we check if this is readable

#print(Employee_file.read())

#print(Employee_file.readline()) #read only the fist line, commen out the above line to se the result
#print(Employee_file.readline())
#print(Employee_file.readline()[0])

for Employees in Employee_file.readline():
    print(Employees)

Employee_file.close()
# close is important
