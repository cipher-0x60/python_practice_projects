# Create simple Create, Read, Update, Delete Program.

# First import the Libraries.
from pathlib import Path

# Read the Current Path and List All The Files
def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} :{items} ")


# Create File Function.
def create_file():
    try:

        readFileAndFolder()
        name = input("Please Tell the File Name:- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What You Want To Write In This File:- ")
                fs.write(data)
            print(f"File Has Been Created Successfully With Name {name}, Data {data}")

    except Exception as err:
        print(f"An Error Occured as {err}")


# Read The File.

def read_file():
    try:

        readFileAndFolder()
        name = input("Tell The Name Of The File Which You Want To Read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = p.read()
                print(data)
        else:
            print("The file does not exists")

    except Exception as err:
        print("An Error Occured as {err}")   















# First Takes the user's input for opration selection.
print("Choose 1 for Creating the file")
print("Choose 2 for Reading the file")
print("Choose 3 for Updating the file")
print("Choose 4 for Deleteing the file")

check = int(input("Plese Choose Your Opreation:- "))

if check == 1:
    create_file()

if check == 2:
    read_file()

if check == 3:
    update_file()

if check == 4:
    delete_file()
