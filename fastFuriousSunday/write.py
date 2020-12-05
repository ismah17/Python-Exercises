"""
employee_file = open("employee.txt", "a")  # type: TextIO
# print(type(employee_file))
employee_file.write("Mark - Tutor")
employee_file.write("\nKelly - SInger")
employee_file.close()

"""
"""
employee_file= open("employee.txt", "w")
# write is going to overwrite whatever the
# file had before
employee_file.write("\nKelly - Singer")
employee_file.close()
"""
employee_file= open("employee1.txt", "w")
# write is going to create a new file
employee_file.write("\nKelly - Singer")
employee_file.close()

employee_file=open("index.html", "w")
employee_file.write("\nIshani's Happy Room\n")
employee_file.write("<p>https://www.youtube.com/watch?v=rfscVS0vtbw&list=PLZG-SuLVGrt7GITt9oOTDd0qnQfYQhfcV&index=19&t=11057s </p>")
employee_file.close()