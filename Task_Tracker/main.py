#The main program
import sys
import os
import my_package.quote_file.quote_module as quote
import my_package.tasks_file.task_module as tasks
import my_package.archive_file.archive_module as archive
import my_package.show_objectives_file.show_objectives_module as show

base_dir = os.path.dirname(os.path.abspath(__file__)) #Make sure program works regardless of path directory
sys.path.insert(0, base_dir)
os.makedirs(os.path.join(base_dir, "current_objectives"), exist_ok=True) #Creates empty folder at startup if folder does not exist
os.makedirs(os.path.join(base_dir, "archive"), exist_ok=True) #Creates empty folder at startup if folder does not exist

print("Welcome to your personal task tracker")
quote.random_quote() #Prints a random quote from quotes.txt everytime the program starts

file_log = show.create_file_log() #A dictionary of file names for easy access

while True:
    file_log = show.create_file_log() #Updates file log every loop in case changes were made

    if file_log == {}: #If the current_objectives folder is empty, the starter menu appears
        print("Create an objective to start. More options will be made available once you have at least one objective.")
        print(
            "\n------------Starter Menu------------\n"
            "[1] Create new Objective\n"
            "[2] Add random quote to quote generator\n"
            "[3] Shut down tracker")
        
        while True:# Choosing number on starter menu
            try: # Error checking to make sure input is valid
                choice = int(input("Choose an action: "))
                if choice < 1 or choice > 3:
                    print("Not a number on the menu. Try again")
                    continue
                break
            except:
                print("Not a valid entry. Try again")
        #Convert starter menu choices to main menu choices for use on if statements later
        if choice == 1:
            choice = 3
        elif choice == 2:
            choice = 5
        elif choice == 3:
            choice = 6
    else: #If there is at least one objective in the current_objectives file, show full menu
        print(
        "\n------------Main Menu------------\n"
        "[1] Show current objectives\n"
        "[2] Update an objective\n"
        "[3] Create new Objective\n"
        "[4] Archive an objective\n"
        "[5] Add random quote to quote generator\n"
        "[6] Shut down tracker")
    
        while True:# Choosing number on main menu
            try: # Error checking to make sure input is valid
                choice = int(input("Choose an action: "))
                if choice < 1 or choice > 6:
                    print("Not a number on the menu. Try again")
                    continue
                break
            except:
                print("Not a valid entry. Try again")

    if choice == 1:
        #Shows files and show an objective of your choice
        if file_log != {}:
            show.show_files(file_log)
            objective_choice = show.file_log_choice("What objective would you like to view?\n")
            print(f"\n----------{file_log[objective_choice]} Tasks----------")
            show.show_tasks(file_log[objective_choice])
        else:
            print("No objectives to show. Create an objective to start")
    elif choice == 2:
        #update file, delete tasks, add tasks or update completion status
        show.show_files(file_log)
        file_choice = show.file_log_choice("What objective would you like to edit?\n")
        file_name = f"\n----------{file_log[file_choice]} Tasks----------"
        file_access = "current_objectives/" + file_log[file_choice]
        edited_content = tasks.edit_tasks(file_access, file_name)
        tasks.write_file(file_log[file_choice], edited_content)
    elif choice == 3:
        #Create new objective (new file)
        while True:
            file_name = input("What is the objective's name?\n")
            if len(file_name) > 30 or not file_name.strip(): #The new file name cannot be longer than 30 character and must not be empty or only whitespaces
                print("File name must be under 30 characters long and cannot be empty")
                continue
            else:
                break   
        print(f"----------Adding tasks for {file_name}----------")
        task = tasks.task_creator(1, [])
        tasks.write_file(file_name, task)
    elif choice == 4:
        #Archive a file (Move to archive folder)
        show.show_files(file_log)
        archive_choice = show.file_log_choice("Which objective would you like to archive?\n")
        archive.archive_file(file_log[archive_choice]) 
        print(f"{file_log[archive_choice]} has been moved to the archive folder.")
    elif choice == 5:
        #Add a quote to quotes.txt to be randmoly displayed on startup
        new_quote = input("What is the quote you want to add?\n")
        quote.add_quote(new_quote)
        print("Quote added...")
    elif choice == 6:
        #Shut down program
        print("Shutting down..")
        sys.exit()

