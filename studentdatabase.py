def manage_student_database():
    # Step 1: Initialize the Program and Create a Function
    student_list = []  # List to store student tuples
    student_id = 1  # Counter for student IDs

    # Step 2: Handle User Input
    while True:
        student_name = input("Enter student name (or 'stop' to finish): ")
        
        if student_name.lower() == "stop":
            break  # End the input process
        
        # Step 3: Check for Duplicate Names
        if any(name == student_name for _, name in student_list):
            print(f"Duplicate name '{student_name}' found. Please enter a different name.")
            continue  # Skip to the next iteration
        
        # If not a duplicate, add the student
        student_tuple = (student_id, student_name)
        student_list.append(student_tuple)
        student_id += 1  # Increment student ID for the next entry

    # Step 4: Display Complete List of Students
    print("\nComplete list of students:")
    print(student_list)

    # Step 5: Display Each Student's ID and Name Individually
    print("\nStudents:")
    for sid, name in student_list:
        print(f"ID: {sid}, Name: {name}")

    # Step 6: Calculate and Display Statistics
    total_students = len(student_list)
    total_length_names = sum(len(name) for _, name in student_list)
    
    if total_students > 0:
        longest_student = max(student_list, key=lambda x: len(x[1]))
        shortest_student = min(student_list, key=lambda x: len(x[1]))

        print(f"\nTotal number of students: {total_students}")
        print(f"Total length of all student names combined: {total_length_names}")
        print(f"Student with the longest name: ID: {longest_student[0]}, Name: {longest_student[1]}")
        print(f"Student with the shortest name: ID: {shortest_student[0]}, Name: {shortest_student[1]}")
    else:
        print("\nNo students were added.")

# Step 7: Call the manage_student_database() Function
if __name__ == "__main__":
    manage_student_database()
