"""
class Wages:
    def __init__(self, unit_wage, name):
        self.unit_wage = unit_wage
        self.name = name

"""


class Wages:
    def __init__(self, unit_wage, work_hours):
        self.unit_wage = unit_wage
        self.work_hours = work_hours

    def Salary(self):
        salary = self.unit_wage * self.work_hours
        return salary


