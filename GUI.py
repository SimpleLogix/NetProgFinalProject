# GUI.py
# FINAL PROJECT FOR NETWORK CLASS

# ----------------------------Necessary imports
from tkinter import *
import tkinter.messagebox as box
import tkinter.font as tkFont
#from gui.styles.fonts import *

# ----------------------------Global variables
username = ''
# import in client.py module

current_question = 'asdfsaf'
a1 = 'asd'
a2 = 'asd'
a3 = 'asd'
a4 = 'asd'
questions_left = 2 # Show score when all questions are answered
score = 0
# ----------------------------Global constants
NAME_OF_THE_GAME = 'Friendly Feud'
WINDOW_SIZE = '500x500'

# ----------------------------Main window---------------------------------------
root = Tk()
root.title(NAME_OF_THE_GAME)
root.geometry(WINDOW_SIZE)

# ----- Store an integer as a picked choice identifier
v = IntVar()
#------------------------------Styles
# Font styles
questionFontSize = tkFont.Font(family="Lucida Grande", size=18)
submitButtonFontSize = tkFont.Font(family="Helvetica", size=12)


# ---------------------------Username frame-------------------------------------
usernameFrame = Frame(root)
label_username = Label(usernameFrame,text='Username:').grid(row=0,column=1)
# Hold username
uString = StringVar()
# Entry to ask for a username
userNameEntry = Entry(usernameFrame,textvariable=uString,width=20).grid(row=0,column=2)


def remove_frame(frame):
    '''Remove specified frame'''
    frame.grid_forget()
    
def set_username():
    '''Get text from the entry and send it to the server'''
    global username
    username = uString.get()
    print(username)
    # Remove username frame
    remove_frame(usernameFrame)


    
# Button to set username
button_get_username = Button(usernameFrame, text="Submit",
                          bg='white',
                          padx=5,
                          bd=0,
                          command=set_username).grid(row=0,column=3)

usernameFrame.grid(row=0,column=1)
# ------------------------------------------------------------------------------

# -----------------------------------Leaderboard frame--------------------------

leaderboard_frame = Frame(root)
player_one_label = Label(leaderboard_frame,text='Player 1').grid(row=0, column=0)
player_one_score = Label(leaderboard_frame,text='Score 100').grid(row=0, column=1)
player_two_label = Label(leaderboard_frame,text='Player 2').grid(row=1, column=0)
player_two_score = Label(leaderboard_frame,text='Score 200').grid(row=1, column=1)
player_three_label = Label(leaderboard_frame,text='Player 3').grid(row=2, column=0)
player_three_score = Label(leaderboard_frame,text='Score 300').grid(row=2, column=1)

button_close_leaderboard = Button(leaderboard_frame, text="Submit",
                              bg='white',
                              padx=5,
                              bd=0,
                              command=remove_frame(leaderboard_frame)).grid(row=0,column=3)

# ------------------------------------------------------------------------------


# -----------------------------------Question frame-----------------------------
question_frame = Frame(root)
question_label = Label(question_frame,text=current_question,font=questionFontSize).grid(row=0,column=0)

first = Radiobutton(question_frame,text=a1,
                        variable=v,
                        indicatoron=0,
                        padx=20,
                        pady=2,
                        width=20,
                        bd=0,
                        height=4,
                        value=1).grid(row=1,column=1)

second = Radiobutton(question_frame,text=a2,
                         variable=v,
                         indicatoron=0,
                         padx=20,
                         width=20,
                         bd=0,
                         height=4,
                         value=2).grid(row=2,column=1)

third = Radiobutton(question_frame,text=a3,
                        variable=v,
                        indicatoron=0,
                        padx=20,
                        width=20,
                        bd=0,
                        height=4,
                        value=3).grid(row=3,column=1)

fourth = Radiobutton(question_frame,text=a4,
                         variable=v,
                         indicatoron=0,
                         padx=20,
                         width=20,
                         bd=0,
                         height=4,
                         value=4).grid(row=4,column=1)


# Submit button handler
# Send the value from the checkbox to the server
def sendToServer():
    '''This function sends an answer to the server'''
    global questions_left,score,v
    
    # Case when no answer given
    if v.get() == 0:
        box.showinfo('Oops...','Have to pick one of the provided answers')

    # Answer is given
    else:
         questions_left -= 1
         box.showinfo('Sent to the server','Your answer sent to the server')
         print('Questions left to answer: ', questions_left)
         print(v.get())# Will print which number was selected
         v.set(0) # reset the selection for the next question

    # Decide when to show score
    if questions_left == 0:
        remove_frame(question_frame)
        print('Show leaderboard here')
        leaderboard_frame.grid(row=0,column=1)
        box.showinfo('Your score is', str(score))
        questions_left = 2
    
#-----------------------------Submit button
submitButton = Button(question_frame, text="Submit",
                          bg='white',
                          padx=20,
                          width=20,
                          height=3,
                          bd=0,
                          command=sendToServer).grid(row=6,column=2)


# ------------------------------------------------------------------------------


# ----------------------------Assign questions and anwers from the server ----
def startGame():
    # Show questions
    question_frame.grid(row=0,column=1)
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
