import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__)) #Make sure program works regardless of path directory
sys.path.insert(0, base_dir)

def create_file_log(): #Creates a dictionary of the files with key values for easy access
    i = 0
    file_dict = {}
    
    files = os.listdir(os.path.join(base_dir, "..", "..", "current_objectives"))
    for file in files: #Create numbers next to files for easy access
        i += 1
        file_dict[str(i)] = file #Adds entry of file to dictionary with a key
    return file_dict

def show_files(log): #Show the files in file_log dictionary and display progress bar
    print(f"{"\n----------Current Objectives----------":<40}-----------Progress------------")
    for i in log:
        with open(os.path.join(base_dir, "..", "..", "current_objectives", log[i]), "r") as file:
            complete_tasks = int(file.readline()) #Reads frist line with int of how many tasks are complete
            total_tasks = int(file.readline()) #Reads second line with int of total number of tasks in file

        if total_tasks != 0: #If there are tasks in the file, proceed to compute percentage and make progress bar
            percentage = round((complete_tasks / total_tasks) * 100)
            progress_bar_complete = round(20 * (percentage / 100)) #Count the progress side "|||||"
            progress_bar_rest = 20 - progress_bar_complete #Count the empty side "----"
            progress_bar = "["
            for j in range(progress_bar_complete):
                progress_bar += "|"
            for k in range(progress_bar_rest):
                progress_bar += "-"
            progress_bar += f"]  {percentage}%"
        else: #If there are no tasks in the file, progress bar will be replaced with "EMPTY"
            progress_bar = "EMPTY"
        
        text = f"[{i}] {log[i]}"
        print(f"{text:<40} {progress_bar}")

def show_tasks(objective): #Displays the tasks in the file
    task_dict = {} #Tasks are put in a dictionary for easy name access
    counter = 0 # Counts amount of tasks in file
    with open(os.path.join(base_dir, "..", "..","current_objectives/") + objective, "r") as file: #Reads the file and skips first 2 lines (Progress bar information only)
        for i in file:
            counter += 1
            if counter > 2:
                task_dict[counter - 2] = i.rstrip()

    for i in task_dict: #Prints the tasks in task_dict dictionary
        print(f"[{i}] {task_dict[i].rstrip()}")

def file_log_choice(message): #This functions is to make sure the user chooses an option in the dictionary and handles it correctly if the user doesn't
    file_log = create_file_log() 
    while True:
        file_choice = input(message)
        if file_choice not in file_log:
            print("Invalid choice, try again..")
            continue
        else:
            return file_choice