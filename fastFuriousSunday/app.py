from classesAndObjects import Student


student1 = Student("ishani", "business", 3.1, False)
student2 = Student("ishaniD", "science", 3.3, True)
print(student1.name)
print(student2.gpa)

print(student2.on_honor_roll())