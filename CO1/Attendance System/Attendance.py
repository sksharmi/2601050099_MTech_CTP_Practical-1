import csv
import os
from datetime import datetime

FILE_NAME = "attendance.csv"


# -----------------------------
# Create CSV file if not exists
# -----------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Student ID", "Student Name", "Status"])


# -----------------------------
# Add Student
# -----------------------------
def add_student():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    students_file = "students.csv"

    if not os.path.exists(students_file):
        with open(students_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Student Name"])

    with open(students_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, student_name])

    print("Student added successfully!")


# -----------------------------
# Display Students
# -----------------------------
def get_students():
    students_file = "students.csv"

    if not os.path.exists(students_file):
        print("No students found.")
        return []

    students = []

    with open(students_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


# -----------------------------
# Mark Attendance
# -----------------------------
def mark_attendance():
    students = get_students()

    if not students:
        return

    date = datetime.now().strftime("%Y-%m-%d")

    print("\nMark Attendance")
    print("----------------")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        for student in students:

            while True:
                status = input(
                    f"{student['Student ID']} - "
                    f"{student['Student Name']} (P/A): "
                ).upper()

                if status in ["P", "A"]:
                    break

                print("Please enter P for Present or A for Absent.")

            if status == "P":
                status = "Present"
            else:
                status = "Absent"

            writer.writerow([
                date,
                student["Student ID"],
                student["Student Name"],
                status
            ])

    print("\nAttendance marked successfully!")


# -----------------------------
# View Attendance
# -----------------------------
def view_attendance():
    if not os.path.exists(FILE_NAME):
        print("No attendance records found.")
        return

    print("\nAttendance Records")
    print("-" * 70)

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(
                f"Date: {row['Date']} | "
                f"ID: {row['Student ID']} | "
                f"Name: {row['Student Name']} | "
                f"Status: {row['Status']}"
            )


# -----------------------------
# Attendance Percentage
# -----------------------------
def attendance_percentage():
    students = get_students()

    if not students:
        return

    student_id = input("Enter Student ID: ")

    total = 0
    present = 0
    student_name = ""

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Student ID"] == student_id:

                total += 1
                student_name = row["Student Name"]

                if row["Status"] == "Present":
                    present += 1

    if total == 0:
        print("No attendance records found for this student.")
        return

    percentage = (present / total) * 100

    print("\nAttendance Report")
    print("------------------")
    print("Student ID:", student_id)
    print("Student Name:", student_name)
    print("Total Classes:", total)
    print("Present:", present)
    print("Absent:", total - present)
    print(f"Attendance Percentage: {percentage:.2f}%")


# -----------------------------
# Main Menu
# -----------------------------
def main():

    initialize_file()

    while True:

        print("\n==============================")
        print("   ATTENDANCE MANAGEMENT")
        print("==============================")

        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Attendance Percentage")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            mark_attendance()

        elif choice == "3":
            view_attendance()

        elif choice == "4":
            attendance_percentage()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    main()