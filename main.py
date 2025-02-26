import inquirer
import random

# Welcome message
print("Wellcome to my Student Management System SMS!!!!!!")

# Dictionary to store students' data
students_data = {
    "name": [],
    "father_name": [],
    "age": [],
    "student_id": [],
}

# Function to generate a random student ID
def generate_student_id():
    return random.randint(1000,9999)

# Main loop to keep the program running
while True:

    # Get prompt user with options by using inquirer Package
    questions = [
        inquirer.List("confirmation",
                      message="What do you want to do?",
                      choices=["Registeration", "Check Result", "All Students Data", "Check Compulsory Subjects", "Exit"],)
    ]
    answer = inquirer.prompt(questions)
    res = answer['confirmation']
    
    # Handle user selection
    if res == "Registeration":

        # Collect student information through user input
        student_name = input("Enter Your Name: ")
        student_father_name = input("Father Name: ")
        student_age = int(input("Enter Your age: "))
        
        # Check if the student is eligible to registeration
        if student_age <= 25:
            student_sure = input("Are you sure to submit your entered data? (yes/no): ")
            if student_sure == "yes":
                # Save student data
                students_data["student_id"].append(generate_student_id())
                students_data["name"].append(student_name)
                students_data["father_name"].append(student_father_name)
                students_data["age"].append(student_age)
                print("Data Submitted Successfully")
            else:
                print("Data Not Submitted")
        else:
            print("You are not allowed to register in this system")
    
    elif res == "Check Result":

        # Placeholder for result checking functionality
        print("Result Checking is in Progress!!!")
    
    elif res == "All Students Data":

        # Display all students' data
        print("All Students Data displayed below")
        print("Student ID: ", students_data["student_id"])
        print("Name: ", students_data["name"])
        print("Father Name: ", students_data["father_name"])
        print("Age: ", students_data["age"])
    
    elif res == "Check Compulsory Subjects":
        
        # Display compulsory subjects
        compulory_subjects = ("Maths", "Physics", "Chemistry", "English", "Urdu")
        print("Compulsory Subjects are: ", compulory_subjects)
    
    elif res == "Exit":
        
        # Exit the program
        print("Exiting the System")
        break
