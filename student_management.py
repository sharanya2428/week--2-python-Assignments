import csv
import os

file = "students.csv"

if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        csv.writer(f).writerow(["Name", "Roll", "Marks"])

while True:
    print("\n1.Add  2.Search  3.Delete  4.Display  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Name: ")
        roll = input("Roll No: ")
        marks = input("Marks: ")

        with open(file, "a", newline="") as f:
            csv.writer(f).writerow([name, roll, marks])
        print("Student added")

    elif ch == 2:
        roll = input("Enter Roll No: ")
        found = False

        with open(file, "r") as f:
            for row in csv.DictReader(f):
                if row["Roll"] == roll:
                    print(row)
                    found = True

        if not found:
            print("Student not found")

    elif ch == 3:
        roll = input("Enter Roll No: ")
        rows = []

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        rows = [r for r in rows if r["Roll"] != roll]

        with open(file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Roll", "Marks"])
            writer.writeheader()
            writer.writerows(rows)

        print("Deleted")

    elif ch == 4:
        with open(file, "r") as f:
            for row in csv.reader(f):
                print(row)

    elif ch == 5:
        break
