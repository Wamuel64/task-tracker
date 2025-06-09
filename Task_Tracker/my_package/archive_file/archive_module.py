import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__)) #Make sure program works regardless of path directory
sys.path.insert(0, base_dir)

def archive_file(name):  #Creates a new file with progress num in first line, task counter num in second line and all tasks afterwards.
    #Read content of the old file and put in a list
    with open(os.path.join(base_dir, "..", "..","current_objectives", name), "r") as old_file:
        content = old_file.readlines()
        content = content[2:]

    with open(os.path.join(base_dir, "..", "..", "archive", name), "w") as file: #Name is the name of the file, content will be a list with tasks input of user
        progress = 0
        task_counter = 0
        for i in content: #Count how many "|" if any and count the amount of tasks
            task_counter +=1
            if i[0] == "|":
                progress += 1

        file.write(f"{progress}\n") #This will represent the progress bar  
        file.write(f"{task_counter}\n") #The next line will represent the total number of tasks for computing the percentage

        for i in content: #Writes tasks after progress and task counter
            file.write(i)

    os.remove(os.path.join(base_dir, "..", "..", "current_objectives", name)) #Remove objective from current_objectives folder