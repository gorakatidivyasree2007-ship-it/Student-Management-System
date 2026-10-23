students = {}

while True:
    name = input("Student name (or exit): ")
    if name.lower() == "exit":
        break

    marks = float(input("Enter marks: "))
    students[name] = marks

for name, marks in students.items():
    print(f"{name}: {marks} marks")
