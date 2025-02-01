# This program is intended on practicing JSON file handling in Python.

import json

json_file = "student.json"

def load_students(student.json):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Creating a new one.")
        return []  # Return an empty list if the file doesn't exist

def print_students(student_list, message):
    print("\n" + message)
    print("-" * 50)
    if not student_list:  # Check if the list is empty
        print("No students found.")
    else:
        for student in student_list:
            print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")
    print("-" * 50)

def append_new_student(student_list):
    new_student = {
        "F_Name": "YourFirstName",  # Replace with actual first name
        "L_Name": "YourLastName",  # Replace with actual last name
        "Student_ID": 99999,  # Replace with actual student ID
        "Email": "your.email@example.com",  # Replace with actual email
    }
    student_list.append(new_student)

def save_students(file_path, student_list):
    with open(file_path, "w") as file:
        json.dump(student_list, file, indent=4)
    print(f"\nThe '{file_path}' file has been updated.")

# --- Main Execution ---

students = load_students(json_file)

print_students(students, "Original Student List:")

append_new_student(students)

print_students(students, "Updated Student List:")

# Ask user if they want to save the changes
while True:
    choice = input("\nWould you like to save changes to student.json? (yes/no): ").strip().lower()
    if choice == "yes":
        save_students(json_file, students)
        print("\nChanges saved successfully.")
        break
    elif choice == "no":
        print("\nChanges discarded. Exiting program.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")