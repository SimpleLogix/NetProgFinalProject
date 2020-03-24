# GUI.py
# FINAL PROJECT FOR NETWORK CLASS

# ----------------------------Necessary imports
from tkinter import *
import tkinter.messagebox as box
import tkinter.font as tkFont
import tkinter as tk

# ----------------------------Global variables
v = ''
currentQuestion = ''
a1 = ''
a2 = ''
a3 = ''
a4 = ''
questionsLeft = 10 # Show score when all questions are answered
score = 0
# ----------------------------Global constants
NAME_OF_THE_GAME = 'Friendly Feud'
WINDOW_SIZE = '500x500'

# ----------------------------Create a barebone of the TKinter project

root = Tk()
root.title(NAME_OF_THE_GAME)
root.geometry(WINDOW_SIZE)
# Image placeholder


#------------------------------Styles
# Font styles
questionFontSize = tkFont.Font(family="Lucida Grande", size=18)
submitButtonFontSize = tkFont.Font(family="Helvetica", size=12)


# Send the value from the checkbox to the server
def sendToServer():
    '''This function sends an answer to the server'''
    global questionsLeft,score
    
   
    # Case when no answer given
    if v.get() == 0:
        box.showinfo('Oops...','Have to pick one of the provided answers')

    # Answer is given
    else:
         questionsLeft -= 1
         box.showinfo('Sent to the server','Your answer sent to the server')
         print('Questions left to answer: ', questionsLeft)
         print(v.get())# Will print which number was selected
         v.set(0) # reset the selection for the next question

    # Need to know how the client will sent information to the server
    # ...
    # ...
    # and include the answer(1,2,3,4) into the message
    
    # Decide when to show score
    if questionsLeft == 0:
        print('Show leaderboard here')
        box.showinfo('Your score is', str(score))


# Need to click start game button to see the question with answers
def gameStartedState():
    '''The game is started
       All of the UI components are initialized
    '''
    global v,currentQuestion
    # The question from the server will be inserted into the labe's text
    lenterNumber = Label(root,text=currentQuestion,font=questionFontSize)
    lenterNumber.pack(side=TOP)
 
    v = IntVar() # used to indicate which value was selected in the radiobuttons

    first = Radiobutton(root,text=a1,
                        variable=v,
                        indicatoron=0,
                        padx=20,
                        pady=2,
                        width=20,
                        bd=0,
                        height=4,
                        value=1)

    second = Radiobutton(root,text=a2,
                         variable=v,
                         indicatoron=0,
                         padx=20,
                         width=20,
                         bd=0,
                         height=4,
                         value=2)

    third = Radiobutton(root,text=a3,
                        variable=v,
                        indicatoron=0,
                        padx=20,
                        width=20,
                        bd=0,
                        height=4,
                        value=3)

    fourth = Radiobutton(root,text=a4,
                         variable=v,
                         indicatoron=0,
                         padx=20,
                         width=20,
                         bd=0,
                         height=4,
                         value=4)

    #Make all of them visible
    first.pack(fill=X)
    second.pack(fill=X)
    third.pack(fill=X)
    fourth.pack(fill=X)

    #-----------------------------Submit button
    #Should send the answer back to the server
    submitButton = Button(root, text="Submit",
                          bg='white',
                          padx=20,
                          width=20,
                          height=3,
                          bd=0,
                          command=sendToServer)
    submitButton.pack()

# ----------------------------Assign questions and anwers from the server
def startGame():
    global currentQuestion,a1,a2,a3,a4
    
    # Assign question and answers from the server
    currentQuestion = 'Get it from the server and assign here'
    a1 = 'Answer from the server 1'
    a2 = 'Answer from the server 2'
    a3 = 'Answer from the server 3'
    a4 = 'Answer from the server 4'
    
    # Initialize UI components
    gameStartedState()
    '''Start the game. This command will request a question from the server'''
    box.showinfo('New game','The game is about to start')  

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
        box.showinfo('Exiting','Come back soon!')
        root.destroy()

# ----------------------------Create a menu
menu = Menu(root)
root.config(menu=menu)

choice = Menu(menu)
menu.add_cascade(label=NAME_OF_THE_GAME,menu=choice)

choice.add_command(label='Start the game',command=startGame)
choice.add_command(label='Instruction', command=showInstruction)
choice.add_command(label='Credits', command=showCredits)
choice.add_separator()
choice.add_command(label='Exit', command=exitTheProgram)

# ----------------------------Show main window
root.mainloop()
