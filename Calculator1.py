### ------------------ IMPORT LIBRARIES ----------------- ####
from tkinter import *
from functools import reduce
master = Tk()

##### ----------------- INSERTION FUNCTIONS ----------------- ####

# if the symbol is clicked, insert operator into the entry bar. 
def add():
    e.insert(END, "+")

def subtract():
    e.insert(END, "-")
    
def multiply():
    e.insert(END, "*")

def divide():
    e.insert(END, "/")
    
##### ------------------ OPERATIONAL FUNCTIONS ------------- #######
##### perform calculative operation based on desired function to be performed
##### on numbers.

#####-------------------Addition----------------------------#########
    
def addL():
    # We receive information
    Data = e.get()

    # Remove the operation sign from the data 
    num = Data.split("+")   
    total = 0

    # List enumeration
    nums = [float(i) if '.' in i else int(i) for i in num]
    
    # Ability to add any new elements in the calculated entry.
    
    print("Sum of all elements in given list: ", sum(nums))
    
        


          
######--------------------Subtraction----------------------------------########

def subL():

    # We receive information
    Data = e.get()

    
    #Remove the operation sign from the data
    num = Data.split("-")   
    total = 0
    nums = [float(i) if '.' in i else int(i) for i in num]
    
    #Biggest number from the list
    
    max_num = max(nums)
    #print(max_num)
    
    #print (nums)
    
    # Ability to subtract any new elements in the calculated entry.
    
    nums.remove(max_num)
    answer = [max_num - i for i in nums]
    print (answer)

######--------------------Division----------------------------#######

    
def divL():

    # We receive information
    Data = e.get()

    
    #Remove the operation sign from the data
    num = Data.split("/")   
    total = 0
    nums = [float(i) if '.' in i else int(i) for i in num]
    
    #Biggest number from the list
    
    max_num = max(nums)
    #print(max_num)
    
    #print (nums)
    
    # Ability to subtract any new elements in the calculated entry.
    
    nums.remove(max_num)
    answer = [max_num / i for i in nums]
    print (answer)


#######-------------------Multiplication----------------------#######

def multL():

    # We receive information
    
    Data = e.get()

    
    # Remove the operation sign from the data
    
    num = Data.split("*")   
    total = 0
    nums = [float(i) if '.' in i else int(i) for i in num]

    # Multiply all the numbers

    import math
    Dub = math.prod(nums)
    print(Dub)



###### DETERMINE WHICH FUNCTION TO EXECUTE BASED ON WHICH OPERATION IS INPUTTED
    
def enter():
    for i in e.get():
        if i == "+":
            addL()
        elif i == "*":
             multL()
        elif i == "/": 
             divL()
        elif i == "-":
             subL()

             
#### ----- INSERT NUMBERS INTO ENTRY BAR BASED ON WHICH BUTTON IS CLICKED ---- #     
def zero():
    e.insert(END, "0")
def one():
    e.insert(END, "1")
def two():
    e.insert(END, "2")
def three():
    e.insert(END, "3")
def four():
    e.insert(END, "4")
def five():
    e.insert(END, "5")
def six():
    e.insert(END, "6")
def seven():
    e.insert(END, "7")
def eight():
    e.insert(END, "8")
def nine():
    e.insert(END, "9")

###### ------------------ DESIGN AND GUI FEATURES --------------- #######
e = Entry(master)
e.grid(row=0, column=1)

b = Button(master, text="0", command=zero)
b.grid(row=3, column=0)

b1 = Button(master, text="1", command=one)
b1.grid(row=3, column=1)

b2 = Button(master, text="2", command=two)
b2.grid(row=3, column=2)

b3 = Button(master, text="3", command=three)
b3.grid(row=4, column=0)

b4 = Button(master, text="4", command=four)
b4.grid(row=4, column=1)

b5 = Button(master, text="5", command=five)
b5.grid(row=4, column=2)

b6 = Button(master, text="6", command=six)
b6.grid(row=5, column=0)

b7 = Button(master, text="7", command=seven)
b7.grid(row=5, column=1)

b8 = Button(master, text="8", command=eight)
b8.grid(row=5, column=2)

b9 = Button(master, text="9", command=nine)
b9.grid(row=6, column=1)

enterN = Button(master, text="ENTER", command=enter)
enterN.grid(row=8, column=0)

addN = Button(master, text="+", command=add)
subtract=Button(master, text="-", command=subtract)
mult = Button(master, text="X", command=multiply)
divideN = Button(master, text="/", command=divide)

addN.grid(row=7, column=4)
subtract.grid(row=7, column=2)
mult.grid(row=8, column=4)
divideN.grid(row=8, column=2)

master.geometry("230x200")
master.title("Calculator")
mainloop()
