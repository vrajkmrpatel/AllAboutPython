students = {'john':['python','Django','DRF'], 'bob':['java','spring'],'jim':['js','react','node']}

# print(students)

keys=students.keys()

for eachKey in students:
      print("Courses taken by", eachKey, " are: ")
      for eachCourse in students[eachKey]:
            print(eachCourse)