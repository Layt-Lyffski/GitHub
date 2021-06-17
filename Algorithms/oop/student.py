class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

   


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False 

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Layt", 19, 95)
s2 = Student("Bill", 19, 85)
s3 = Student("Lify", 18, 98)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())




x = [23,24,5,234,23,523,52,3,5]

mp = filter(lambda i: (i*3) % 2 == 0, x)
print(list(mp))


import os

print(os.getcwd())



#input output files
import csv



# input ouput jpg (differten than .txt)
with open("pic.jpg", "rb") as rf: #rb = read binary
    with open("jpn_copy.jpg", "wb") as wf:
        chunk_size = 4096 #how much pix will it it forwarding the pic
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



            """
What is a Package?

A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

            """

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close() 