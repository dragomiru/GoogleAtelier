### Week 3 Homework: To-do list ###
from datetime import datetime

def main():
    menu_listing = input("Selectati introducere, listare, sortare, sau filtrare date din meniu: ")

    if menu_listing == "introducere":
        introducere()
    elif menu_listing == "listare":
        listare()
    elif menu_listing == "sortare":
        sortare()
    elif menu_listing == "filtrare":
        filtrare()

def introducere():
    while True:

        # Task insertion and validation for string.
        task = input("Introduceti taskul: ")
        if task.isdigit() and not task.isalpha():
            break

        # Deadline insertion and validation for specific date format.
        deadline = input("Introduceti data limita: ")
        try:
            deadline = datetime.strptime(deadline, "%d.%m.%Y %H:%M")
        except ValueError:
            print("Se accepta doar formatul ZZ-LL-AAAA OO:MM. Va rog reintroduceti.")
            break

        # Responsible person insertion and validation for string.
        person = input("Introduceti persoana responsabila: ")
        if person.isdigit() and not person.isalpha():
            break

        # Category insertion and validation for string.
        category = input("Introduceti categoria taskului: ")
        if category.isdigit() and not category.isalpha():
            break

        # Must open files simultaneously to check if either category or task repeats in their respective files.
        file_categories = open("file_categories.txt", "r+")
        file_everything = open("file_everything.txt", "r+")

        # Reading each line so we can check in check_doubles() if there are doubles.
        category_lines = file_categories.readlines()
        everything_lines = file_everything.readlines()

        # Function to check if doubles are present.
        def check_doubles():
            result = None
            for line in category_lines:
                if category.rstrip() == line.rstrip():
                    result = "CatDoublePresent"
            for line in everything_lines:
                if task.rstrip() in line.rstrip():
                    result = "TaskDoublePresent"
            return result

        # Checking the output from check_doubles(). If either category or task already present, no input in either files.
        if check_doubles() == "CatDoublePresent":
            print("Aceasta categorie deja exista. Va rog reincercati.")
            break
        elif check_doubles() == "TaskDoublePresent":
            print("Acest task deja exista. Va rog reincercati.")
            break
        # Otherwise, insert user's input accordingly.
        else:
            file_categories.write(f"{category}\n")
            file_everything.write(f"{task}, {deadline}, {person}, {category}\n")
            file_categories.close()
            file_everything.close()

        # Ask for another iteration of user input, otherwise exit loop and function.
        if input("Daca doriti sa continuati introducerea, raspundeti cu 'Da': ") == "Da":
            continue
        else:
            break

def listare():
    print("Acestea sunt taskurile introduse pana acum.")
    print("------------------------------------------------------------------")
    print("Task  |  Deadline  |  Person  |  Category")
    # Printing each line from the file that contains everything.
    with open("file_everything.txt", "r+") as file:
        for line in file:
            print("" + line.rstrip())

def sortare():
    while True:

        # User's input for the field they want to sort by.
        sorting_field = input("După care camp ati dori sa sortati? Alegeti 'task', 'deadline', 'person', sau 'category': ")
        if sorting_field.isdigit() and not sorting_field.isalpha():
            break

        # User's input for the way they want to sort by the chosen field.
        asc_desc = input("Doriti sa sortati in ordine ascendenta sau descendenta? Alegeti 'asc' sau 'desc': ")
        if asc_desc.isdigit() and not asc_desc.isalpha():
            break

        # Converting the lines from the text file into a nested list.
        text_lines = []
        with open("file_everything.txt", "r+") as file:
            for line in file:
                text_lines.append(line.rstrip().split(", "))

        # Depending on user's inputs for the field and way to sort by, the output will be in sorted_list.
        sorted_list = None
        if sorting_field == "task":
            if asc_desc == "asc":
                sorted_list = sorted(text_lines, key=lambda x: x[0])
            else:
                sorted_list = sorted(text_lines, key=lambda x: x[0])[::-1]
        elif sorting_field == "deadline":
            if asc_desc == "asc":
                sorted_list = sorted(text_lines, key=lambda x: x[1])
            else:
                sorted_list = sorted(text_lines, key=lambda x: x[1])[::-1]
        elif sorting_field == "person":
            if asc_desc == "asc":
                sorted_list = sorted(text_lines, key=lambda x: x[2])
            else:
                sorted_list = sorted(text_lines, key=lambda x: x[2])[::-1]
        elif sorting_field == "category":
            if asc_desc == "asc":
                sorted_list = sorted(text_lines, key=lambda x: x[3])
            else:
                sorted_list = sorted(text_lines, key=lambda x: x[3])[::-1]

        print("Acestea sunt taskurile introduse pana acum.")
        print("------------------------------------------------------------------")
        print("Task  |  Deadline  |  Person  |  Category")
        #  A generator that will, for every sublist `sub`, generate a string by joining the elements together with
        #  spaces between them. Advice taken from: https://stackoverflow.com/a/45400619
        print("\n".join(", ".join(sub_list) for sub_list in sorted_list))
        break

def filtrare():
    pass

main()

