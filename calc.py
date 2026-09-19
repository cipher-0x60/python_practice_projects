# Calculator

print("Choose 1 for Addition")
print("Choose 2 for substraction")
print("Choose 3 for division")
print("Choose 4 for multipication")
print("Choose 5 for modules")

opration = int(input("Please Tell Your Opreation:- "))

def opration_checks():
    if opration < 1 or opration > 5:
         print("Please Specify a Valid Operation")
         exit()
opration_checks()

num_1 = int(input("Tell your First number:- "))
num_2 = int(input("Tell your Second number:- "))



def add_num(num_1,num_2):
    print(f"The Sum Of The Given Num {num_1}, {num_2} is {num_1 + num_2} ")

def substract_num(num_1,num_2):
    print(f"substraction of {num_1} and {num_2} is {num_1 - num_2}")

def divid_num(num_1,num_2):
    try:
         result = num_1 / num_2 
         print(f"division of your given number {num_1}, {num_2} is {result}")
    
    except Exception as err:
         print(f"An error Occurred AS {err} ")
         
def multi_num(num_1,num_2):
    print(f"Multipication of Your Given Numbers {num_1}, {num_2} Is {num_1 * num_2} ")


def modules_num(num_1,num_2):
    try:
        result= num_1 % num_2
        print(f"Mod of given Numbers {num_1}, {num_2} Is {result} ")
    
    except Exception as err:
        print(f"An Error Occured as {err} ")




if opration == 1:
    add_num(num_1, num_2)

elif opration == 2:
    substract_num(num_1, num_2)

elif opration == 3:
    divid_num(num_1, num_2)

elif opration == 4:
    multi_num(num_1, num_2)

elif opration == 5:
    modules_num(num_1, num_2)

    
