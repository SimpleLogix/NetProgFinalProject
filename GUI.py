# GUI.py
# FINAL PROJECT FOR NETWORK CLASS

# ----------------------------Necessary imports
from tkinter import *
import tkinter.messagebox as box

# ----------------------------Create a barebone of the TKinter project

root = Tk()
root.title('Justice and Morality')
root.geometry('500x500')

# ----------------------------Create Question
#holds current question
currentQuestion = ''
# The question from the server will be inserted into the labe's text
lenterNumber = Label(root,text='How many oranges you see?')
lenterNumber.pack(side=TOP)   

# ----------------------------Create Answers
# Should fetch answers from the server for the current question
# Value of 1,2,3,4 can serve as an indicator of the correct answer
v = IntVar() # used to indicate which value was selected in the radiobuttons
first = Radiobutton(root,text="Correct answer",variable=v,indicatoron=0,padx=20,width=20,value=1)
second = Radiobutton(root,text="Two oranges",variable=v,indicatoron=0,padx=20,width=20,value=2)
third = Radiobutton(root,text="Three oranges",variable=v,indicatoron=0,padx=20,width=20,value=3)
fourth = Radiobutton(root,text="Four oranges answer",variable=v,indicatoron=0,padx=20,width=20,value=4)

#Make all of them visible
first.pack()
second.pack()
third.pack()
fourth.pack()

# Send the value from the checkbox to the server
def sendToServer():
    '''This function sends an answer to the server'''
   
    # Case when no answer given
    if v.get() == 0:
        box.showinfo('Oops...','Have to pick one of the provided answers')
    else:
         box.showinfo('Sent to the server','Your answer sent to the server')
         print(v.get())# Will print which number was selected
         v.set(0) # reset the selection for the next question

    # Need to know how the client will sent information to the server
    # ...
    # ...
    # and include the answer(1,2,3,4) into the message
    
#-----------------------------Submit button
#Should send the answer back to the server
submitButton = Button(root, text="Submit",padx=20,command=sendToServer)
submitButton.pack()

# ----------------------------Functions

# ----------------------------Server related

def startGame():
    '''Start the game. This command will request a question from the server'''
    box.showinfo('New game','The game is about to start')
    currentQuestion = 'Get it from the server and assign here'
    a1 = 'Answer from the server'
    a2 = 'Answer from the server'
    a3 = 'Answer from the server'
    a4 = 'Answer from the server'

# ----------------------------Only used within the GUI
def showInstruction():
    '''Show game instruction'''
    box.showinfo('Instruction','This game instruction would be added...')

def showCredits():
    '''Show credits. List people who created this game'''
    box.showinfo('Credits','This is created by Walid, Daniel, Alex. WDA team')

# ---------------------------Exit from the program
def exitTheProgram():
    '''Destroy the window'''
    var = box.askyesno('Exiting','Are you sure?')
    if var == 1:
        box.showinfo('Exiting','bye bye')
        root.destroy()

# ----------------------------Create a menu
menu = Menu(root)
root.config(menu=menu)

choice = Menu(menu)
menu.add_cascade(label='Justice and Morality',menu=choice)

choice.add_command(label='Start the game',command=startGame)
choice.add_command(label='Instruction', command=showInstruction)
choice.add_command(label='Credits', command=showCredits)
choice.add_separator()
choice.add_command(label='Exit', command=exitTheProgram)

# ----------------------------Show main window
root.mainloop()
