try:
      f = open("myfile","w")
      a, b = [int(x) for x in input("Enter two integers: ").split()]
      c = a/b
      # print(c)
      f.write("Writting %d into file" %c)
except ZeroDivisionError:
      print("Divide by zero in not allowed")
      print("Try to add other integer")
else :
      print("You have added non zero integer")
finally:
      f.close()
      print("File Closed")
print("Code after exception")