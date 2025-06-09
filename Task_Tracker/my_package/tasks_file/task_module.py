import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__)) #Make sure program works regardless of path directory
sys.path.insert(0, base_dir)


def write_file(name, content): #Creates a new file with progress num in first line, task counter num in second line and all tasks afterwards.
    with open(os.path.join(base_dir, "..", "..", "current_objectives", name), "w") as file: #Name is the name of the file, content will be a list with tasks input of user
        progress = 0
        task_counter = 0
        for i in content: #Count how many "|" if any and amount of tasks
            task_counter +=1
            if i[0] == "|":
                progress += 1

        file.write(f"{progress}\n") #This will represent the progress bar  
        file.write(f"{task_counter}\n") #The next line will represent the total number of tasks for computing the percentage of progress bar

        for i in content: #Writes tasks after progress and task counter
            file.write(i + "\n")

def task_creator(choice, content = []): #Takes a choice (adding tasks, editing task or completion status) and content (existing list or not)
    write_tasks = "Y"
    while write_tasks == "Y":
        completion = ""
        while completion != "?" and completion != "|": #User must choose one of two options
            completion = input("Is this task complete? [|] for yes / [?] for no:\n").strip()

        if choice != 3: #If user is not only editing completion status, ask what the task is
            task = completion + " " + input("What is the task?\n")

        if choice == 1: #If adding tasks
            content.append(task) #Adds task to the list
            write_tasks = input("Do you want to add another task? Y/N \n").upper()
        elif choice == 2: #If editing just one task
            content = [task]
            write_tasks = False
        elif choice == 3: #For editing just a tasks completion status
            content = completion + content[1:]
            write_tasks = False

    return content #Returns content to be overwrite the objective's task(s)

#Add, edit, delete tasks. Objective is the file directory being edited. Name is the string file name
def edit_tasks(objective, name):
    task_list = [] #List of all tasks in the file
    counter = 0 # Counts amount of tasks in file
    with open(os.path.join(base_dir, "..", "..", objective), "r") as file: #Reads the file and skips first 2 lines (Progress bar information only)
        for i in file:
            counter += 1
            if counter > 2:
                task_list.append(i.rstrip())

    edit_tasks = "Y"
    while edit_tasks == "Y": #Loop until user doesn't want to edit a task anymore
        counter = 1
        print(name) #Prints name of file every loop
        for i in task_list: #Prints the tasks in the list
            print(f"[{counter}] {i}")
            counter += 1
    
        edit_choice = 0
        while True:
            try:
                edit_choice = int(input("----------Choose an option----------\n"
                                        "[1] Edit a task\n"
                                        "[2] Add a task\n"
                                        "[3] Delete a task\n"
                                        "[4] Edit task completion status\n"))
                if edit_choice not in range(1, 5):
                    print("Not a valid input")
                    continue
                break
            except:
                print("Not a valid input")

        if task_list != [] or edit_choice == 2: #If the task list is empty, you cannot edit or delete tasks, only add a task (choice 2).
            #Edit a task
            if edit_choice == 1:
                task_choice = user_choice_task_editor("edit", task_list)
                edited_task = task_creator(2, [task_list[task_choice]])
                task_list[task_choice] = edited_task[0]
                edit_tasks = input("Do you want to continue editing the objective? Y/N \n").upper()
            #Add a task    
            elif edit_choice == 2:
                task_list = task_creator(1, task_list)
                edit_tasks = input("Do you want to continue editing the objective? Y/N \n").upper()
            #Delete a task
            elif edit_choice == 3:
                task_choice = user_choice_task_editor("delete", task_list)
                del task_list[task_choice]
                print(f"Task {task_choice + 1} deleted")
                edit_tasks = input("Do you want to continue editing the objective? Y/N \n").upper()
            #Edit task completion status
            elif edit_choice == 4:
                task_choice = user_choice_task_editor("edit", task_list)
                task_list[task_choice] = task_creator(3, task_list[task_choice])
                edit_tasks = input("Do you want to continue editing the objective? Y/N \n").upper()
        else:
            print("No tasks to edit! Add a task first")
            continue
    return task_list

#Used to choose task to edit
def user_choice_task_editor(action, the_list): #Action to display text, the_list to make sure user choice is task list within range
    task_choice = 0
    while True: #Ask user which task he would like to edit
        try:
            task_choice = int(input(f"What task would you like to {action}?\n")) - 1
            if task_choice not in range(0, len(the_list)):
                print("Not a valid input")
                continue
            return task_choice
        except:
            print("Not a valid input")


