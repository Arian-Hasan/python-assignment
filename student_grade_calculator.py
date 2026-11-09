name=input("Enter Customer Name: ")
m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
total=m1+m2+m3
avg=total/3
if avg >= 80: grade = "A+"
elif avg >= 70: grade = "A"
elif avg >= 60: grade = "B"
elif avg >= 50: grade = "C"
else: grade = "F"

print(f"\nStudent Name: {name}\nTotal Marks: {total}\nAverage: {avg:.2f}\nGrade: {grade}")