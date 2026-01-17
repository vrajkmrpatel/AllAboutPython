student_info = {
      "name": "John Doe",
      "age" : 23,
      "major": "CS"
}

print(student_info)

# student_info["email"] = "johndoe@gmail.com"
student_info.update({"email" : "johndoe@gmail.com"})
student_info["age"] = 25

del student_info["major"]
print(student_info)