import random
import time
from colorama import Fore, Style
import os
import openpyxl

# Lists
names = []
chosen_name_list_1 = []
finalists = []

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = "/home/ctmworkin/Documents/Employee_Drawing/names.txt"  # Provide the path to your text file
text_data = read_text_file(file_path)

text_data = text_data.replace("\n", "") # replace newline char
#text_data = text_data.replace(" ", "") # replace empty space

split_data = text_data.split(',') # split string
for x in split_data:
    names.append(x)

print(names)

def print_letter_by_letter_RED(text, delay=0.15):
    for char in text:
        print(Fore.RED + char, end='', flush=True)  
        # Use end='' to avoid newline, flush=True to immediately print
        time.sleep(delay)

def print_letter_by_letter_BLUE(text, delay=0.15):
    for char in text:
        print(Fore.BLUE + char, end='', flush=True)  
        # Use end='' to avoid newline, flush=True to immediately print
        time.sleep(delay)

def print_letter_by_letter_GREEN(text, delay=0.3):
    for char in text:
        print(Fore.GREEN + char, end='', flush=True)  
        # Use end='' to avoid newline, flush=True to immediately print
        time.sleep(delay)

os.system("clear")

print("\n\nSelecting Finalists: ")
for x in range(10):
    chosen_name = random.choice(names)
    names.remove(chosen_name)

    time.sleep(1)
    print_letter_by_letter_RED("\n\n" + chosen_name)
    chosen_name_list_1.append(chosen_name)

time.sleep(2)
os.system("clear")

print(Fore.WHITE + "\n\nNarrowing Selection: ")
for x in range(5):
    finalist = random.choice(chosen_name_list_1)
    chosen_name_list_1.remove(finalist)

    time.sleep(1)

    print_letter_by_letter_BLUE("\n\n" + finalist)
    finalists.append(finalist)

time.sleep(2)
os.system("clear")

winner = random.choice(finalists)
print(Fore.WHITE + "THIS YEAR'S GRAND PRIZE WINNER IS: ")
time.sleep(1)
print_letter_by_letter_GREEN("\n" + winner)

input(Fore.WHITE + "\n\n\n\nPress enter to quit...")

