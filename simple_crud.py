# Create simple Create, Read, Update, Delete Program.

# First import the Libraries.
from pathlib import Path

# Read the Current Path and List All The Files
def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} :{item} ")


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
                data = fs.read()
                print(data)
        else:
            print("The file does not exists")

    except Exception as err:
        print(f"An Error Occured as {err}")   


def update_file():
    try:
       
       readFileAndFolder()
       name = input("Tell Which File You Want to Update:- ")
       p = Path(name)
       if p.exists() and p.is_file():
            print("Press 1 for Changing the name of your file")
            print("Press 2 for Oerwriting the file data")
            print("Press 3 for Appendinig some content ini Your file")

            res = int(input("Tell your Option:- "))
            if res == 1:
                name2 = input("tell you new file name:- ")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want ot write this will overwrite the data:- ")
                    fs.write(data)
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want ot write this will append the data:- ")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An error occured as {err}")




def delete_file():
    try:
        readFileAndFolder()
        name = input("Tell Which File Do you want to Delete:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print(f"Your File {name} on the path {p} has been deleted successfully" )
        else:
            print(f"Your Given File Name '{name}' Does not exists. Please Tell The Correct File Name. ")
    except Exception as err:
        print(f"An error Occured as {err}")








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
