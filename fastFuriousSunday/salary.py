"""

from wage import Wages




employee1 = Wages(145, "ISHANI")
employee2 = Wages(110, "JON")
employee = [employee1.name, employee2.name]
print(employee)

def CalculateSalary(NAME, HOURS, SALARY):

    NAME = input("Enter your first name in capital letters")
    HOURS =input("Enter number of hours you worked this month")
    print("your name is {0} and you worked {1} hours".format(NAME, HOURS))
    #print(NAME in employee)

    if NAME in employee:
        print("you are registered in our database")
        if NAME == employee1.name :
            SALARY = int(employee1.unit_wage) * int(HOURS)
            print("YOUR SALARY IS", SALARY)

        if NAME == employee2.name:
            SALARY = int(employee2.unit_wage) * int(HOURS)
            print("YOUR SALARY IS ", SALARY)



CalculateSalary("s", 1,1)

"""
from wage import Wages

name = str(input("enter your name"))
work_hours = int(input("enter your total work hours for month"))
unit_wage = int(input("enter hourly wage"))

employee = Wages(unit_wage, work_hours)

payment = employee.Salary()

print("Hi {0}!".format(name), " your salary for this month is", payment, ".")
