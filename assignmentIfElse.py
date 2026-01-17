math_marks, physics_marks, chem_marks = [int(x) for x in input("Enter the marks of the subjects: ").split()]

if (math_marks >= 35 and physics_marks >= 35 and chem_marks >= 35):
      print("You Passed the exam...")
      average = (math_marks+physics_marks+chem_marks)/3
      print(f"Your Average is: {average:.2f}")
      if (average<=59):
            print("You got a C grade...")
      elif (average>59 and average<=69):
            print("You got a B grade...")
      else :
            print("You got a A grade...")

else:
      print("You failed the exam...")