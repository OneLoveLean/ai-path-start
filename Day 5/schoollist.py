import sys

class_a = ["Alex", "Bob", "Wiktor"]
class_b = ["Arlong", "Stacy", "Volodia"]
class_c = ["Chopper", "Ola", "Maya"]

teacher_password = "thegoodteacher:)123"
student_password = "12345678910"

prof = input("You are teacher or student?: ").lower()

if prof == "teacher":
    password = input("Enter your password: ")
    if password == teacher_password:
        print("Okay, you can enter!")
    else:
        print("Password is incorrect! Please try again")
        sys.exit()

elif prof == "student":
    password = input("Enter your password: ")
    if password == student_password:
        print("Okay, you can enter!")
    else:
        print("Password is incorrect! Please try again")
        sys.exit()

else:
    print("Incorrect role selected!")
    sys.exit()

class_choice = input("Which class you want to see? (A/B/C): ").lower()

if class_choice == "a":
    print(class_a)
elif class_choice == "b":
    print(class_b)
elif class_choice == "c":
    print(class_c)
else:
    print("Class not found")