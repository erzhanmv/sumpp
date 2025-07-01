#task1
import os

path = input("Enter the path: ")

if not os.path.exists(path):
    print("The specified path does not exist.")
else:
    all_items = os.listdir(path)

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("\nOnly directories:")
    for d in directories:
        print(d)

    print("\nOnly files:")
    for f in files:
        print(f)

    print("\nAll directories and files:")
    for item in all_items:
        print(item)

#task2
import os

path = input("Enter the path: ")

print(f"\nChecking access for: {path}")

print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))
#task3
import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("\nThe path exists.")

    filename = os.path.basename(path)

    directory = os.path.dirname(path)

    print("Filename or last part:", filename)
    print("Directory portion:", directory)

else:
    print("\nThe specified path does not exist.")

#task4
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

#task5
items = ['apple', 'banana', 'cherry', 'date']

filename = 'fruits.txt'

with open(filename, 'w') as file:
    for item in items:
        file.write(item + '\n')

print(f"List written to {filename}")

#task6
import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")
        
print("26 files (A.txt to Z.txt) have been created.")

#task7
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

try:
    with open(source_file, 'r') as src:
        with open(destination_file, 'w') as dest:
            for line in src:
                dest.write(line)
    print(f"Contents copied from {source_file} to {destination_file}.")
except FileNotFoundError:
    print("Source file not found. Please check the filename and try again.")

#task8
import os

file_path = input("Enter the path to the file you want to delete: ")

if not os.path.exists(file_path):
    print("The specified path does not exist.")
elif not os.path.isfile(file_path):
    print("The specified path is not a file.")
elif not os.access(file_path, os.W_OK):
    print("You don't have permission to delete this file.")
else:
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except Exception as e:
        print("Error while deleting file:", e)