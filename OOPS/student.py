class Student:

      major = "CSE" # static field

      def __init__(self, rollno, name):
            self.rollno = rollno
            self.name = name

s1 = Student(1, "John")
s2 = Student(2, "Bob")

print(s1.name)
print(s2.name)

print(s1.major)
print(s2.major)
print(Student.major)