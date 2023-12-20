name = input("Enter your name: ")

labGrade = float(input("Enter lab grade: "))
midtermGrade = float(input("Enter midterm grade: "))
finalGrade = float(input("Enter final grade: "))

grade = (labGrade/4) + (midtermGrade*35/100) + (finalGrade*4/10)

print(f"Name: {name}\n"
      f"Lab: {labGrade}\n"
      f"Midterm: {midtermGrade}\n"
      f"Final: {finalGrade}\n"
      f"Last Score: {grade}")
