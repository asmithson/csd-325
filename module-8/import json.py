import json

# Define the absolute path to student.json
json_file = "c:/Users/Owner/my_csd_325/module-8/student.json"

def load_students(file_path):
    """Load students from JSON file or return None if missing/corrupt."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Unable to load '{file_path}'.")
        return None

def save_students(file_path, student_list):
    """Write the updated student list to the JSON file."""
    with open(file_path, "w") as file:
        json.dump(student_list, file, indent=4)
    print(f"The student list has been saved to '{file_path}'.")

def print_students(student_list, message):
    """Print the list of students."""
    print("\n" + message)
    print("-" * 50)
    if not student_list:
        print("No students in the list.")
    else:
        for student in student_list:
            print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")
    print("-" * 50)

def append_new_student(student_list):
    """Ask user if they want to add students and append new student details to the list."""
    while True:
        add_student = input("\nWould you like to add a student? (yes/no): ").strip().lower()
        if add_student == "no":
            print("Exiting program.")
            return  # Exit the function if the user does not want to add a student
        
        elif add_student == "yes":
            try:
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                student_id = int(input("Enter student ID: ").strip())
                email = input("Enter email: ").strip()
                
                new_student = {
                    "F_Name": first_name,
                    "L_Name": last_name,
                    "Student_ID": student_id,
                    "Email": email
                }
                student_list.append(new_student)
                print(f"Student {first_name} {last_name} added.")
            
            except ValueError:
                print("Invalid input. Please enter valid details.")

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# --- Main Program ---
students = load_students(json_file)  # Step 1: Load the student list

if students is None:  # If the file fails to load
    print("Exiting program due to file error.")
else:
    print_students(students, "Original Student List:")  # Step 2: Print original list

    append_new_student(students)  # Step 3: Ask if the user wants to add a student in a loop
    print_students(students, "Updated Student List:")  # Step 4: Print updated list

    # Step 5: Ask user to save or discard changes
    while True:
        choice = input("\nWould you like to save changes to student.json? (yes/no): ").strip().lower()
        if choice == "yes":
            save_students(json_file, students)  # Save the updated list
            print("Changes saved successfully.")
            break
        elif choice == "no":
            print("Changes discarded. Reloading original student list.")
            students = load_students(json_file)  # Reload original list
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print_students(students, "Final Student List:")  # Print the final list
    print("Program finished.")