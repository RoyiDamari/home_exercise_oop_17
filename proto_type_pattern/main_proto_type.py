from student import Student


def main():
    # Create an original student with some data
    original_student = Student(name="Alice", student_id="S12345")
    original_student.add_grade(101, 88.5)
    original_student.add_grade(102, 92.0)

    print("Original student before cloning:")
    print(original_student)
    print("Average grade:", original_student.get_average_grade())
    print()

    # Clone the student (using the prototype pattern)
    cloned_student = original_student.clone()

    # Add a new grade to the cloned student
    cloned_student.add_grade(103, 95.0)

    print("After adding a new grade to the cloned student:")
    print("Cloned student:", cloned_student)
    print("Original student:", original_student)

    # Verify that the original student's grades are unchanged
    print("\nGrades in original student:", original_student.grades)
    print("Grades in cloned student:", cloned_student.grades)


if __name__ == "__main__":
    main()
