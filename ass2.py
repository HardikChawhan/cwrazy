# Custom Exception
class InvalidStudentIDError(Exception):
    pass

# Function that checks if the student ID is valid
def check_student_id(student_id):
    if isinstance(student_id, str):
        if not student_id.isdigit():
            raise InvalidStudentIDError(f"Student ID must contain only digits: {student_id}")
        if len(student_id) != 8:
            raise InvalidStudentIDError(f"Student ID must be exactly 8 digits long: {student_id}")
    else:
        raise InvalidStudentIDError(f"Student ID must be a string of digits, not {type(student_id).__name__}")

    print(f"Student ID {student_id} is valid.")

# Main Code
try:
    student_id_input = input("Enter the student ID (8-digit number): ").strip()

    check_student_id(student_id_input)

except InvalidStudentIDError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Student ID check completed successfully.")
finally:
    print("Student ID validation process finished.")
