import random
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__)) #Make sure program works regardless of path directory
sys.path.insert(0, base_dir)

#Chooses a random quote to print from the quotes.txt file
def random_quote():
    with open(os.path.join(base_dir, "quotes.txt"), "r") as f:
        lines = f.readlines()
    if lines != []: #If the lines list is not empty, proceed to show a random line from quotes.txt
        print("Incoming motivational quote:")
        print(random.choice(lines), end="")

def add_quote(quote): # Option [5] adds a quote to quotes.txt
    with open(os.path.join(base_dir, "quotes.txt"), "a") as f:
        f.write(f"{quote}\n")
