import os
import re

filepath = ""
words = ""
specific_dir = False

print("1. Create '.py' files at specific path " '\n'
      "2. Create '.py' files at current directory")
question = input("Enter 1 or 2: ")

while True:
    if question == "1":
        print()
        print("Example directory: C:\\Users\\smart\\PycharmProjects\\Fundamentals\\13_objects_and_classes_exercise"'\n')
        filepath = input("Enter the directory path in which you want to create the files : "'\n')
        if os.path.exists(filepath):
            specific_dir = True
            break

        else:
            while True:
                if os.path.exists(filepath):
                    specific_dir = True
                    break
                print("Incorrect path! Please enter valid path!")
                filepath = input()
        break

    elif question == "2":
        specific_dir = False
        break
    else:
        print("Wrong input! Try 1 or 2 !")
        question = input("Enter 1 or 2: ")

print("Example task names: 01. Storage02. Weapon03. Catalogue04. Town05. Class06. Inventory07. Articles08. "
      "Vehicle✶09. Movie✶")
print()
words = input("Paste the names of the tasks copied from judge: ")

pattern = r"(\d{2}\.\s([A-Za-z!@#$%^&*_\-,;'`]+\s?)*)"
match = re.findall(pattern, words)

final_list = [x[0].lower().replace(" ", "_").replace(".", "",) for x in match]

if specific_dir:
    for word in final_list:
        # Creating a file at specified location
        with open(os.path.join(filepath, f"{word}.py"), 'w') as fp:
            pass
else:
    # Creating a file at current location
    for word in final_list:
        fp = open(f'{word}.py', 'x')
        fp.close()

print("Done")
