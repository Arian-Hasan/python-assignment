name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python_marks = float(input("Enter Python marks: "))

if (
    math < 0
    or math > 100
    or english < 0
    or english > 100
    or python_marks < 0
    or python_marks > 100
):
  print("\nInvalid marks! Please enter marks between 0 and 100.")
else:
  avg = (math + english + python_marks) / 3

  if avg >= 80:
    grade = "A+"
  elif avg >= 70:
    grade = "A"
  elif avg >= 60:
    grade = "A-"
  elif avg >= 50:
    grade = "B"
  elif avg >= 40:
    grade = "C"
  else:
    grade = "F"

  print(f"\nStudent Name: {name}")
  print(f"Average Marks: {avg:.2f}")
  print(f"Final Grade: {grade}")