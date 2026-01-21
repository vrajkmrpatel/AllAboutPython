f = open("Files/myfile.txt", "w")
print("Enter the Text (Type # when you are done)")
s = ''
while s != '#':
      s = input()
      f.write(s)
f.close()