# 9.1 Writing Grades to a Plain Text File with Additional Comments
def write_grades_to_file(filename):
    """
    Prompts the user to enter grades and writes them to a specified file.
    The function continues to accept grades until the sentinel value '-1' is entered.
  
    Args:
    filename (str): The name of the file where grades will be stored.
    
    """
    with open(filename, "a") as file:
        while True:
            grade = input("Enter a grade (or -1 to quit): ")
            if grade == "-1":
                break
            file.write(f"{grade}\n")

# write_grades_to_file("grades.txt")



# 9.2 Reading Grades from a Plain Text File with Additional Comments
def read_grades_from_file(filename):
    """
    Reads grades from a specified file, calculates the total, count, and average,
    and handles errors such as missing files or invalid data.
    Also, displays the total of grades, number of grades, and the average grade.    
 
    Args:
    filename (str): The name of the file from which grades will be read.
    
    """
    try:
        with open(filename, "r") as file:
            total = 0
            count = 0
            for line in file:
                grade = int(line.strip())
                total += grade
                count += 1
            if count > 0:
                average = total / count
                print(f"Total: {total}, Count: {count}, Average: {average:.2f}")
            else:
                print("No grades to average.")
    except FileNotFoundError:
        print("The file does not exist.")
    except ValueError:
        print("The file contains non-integer values.")

# read_grades_from_file("grades.txt")



# 9.3 Writing Student Records to a CSV File with Additional Comments
import csv

def write_student_records_to_csv(filename):
    """
    Prompts the user for student records and writes them to a CSV file.
    Each record includes the student's first name, last name, and grades for three exams.
    Writing continues until 'quit' is entered as a first name.
    
    Args:
    filename (str): The name of the CSV file where student records will be stored.

    """
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        while True:
            firstname = input("Enter student's first name (or type 'quit' to stop): ")
            if firstname.lower() == 'quit':
                break
            lastname = input("Enter student's last name: ")
            exam1grade = input("Enter grade for exam 1: ")
            exam2grade = input("Enter grade for exam 2: ")
            exam3grade = input("Enter grade for exam 3: ")
            writer.writerow([firstname, lastname, exam1grade, exam2grade, exam3grade])
