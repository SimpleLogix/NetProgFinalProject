# GUI.py
# FINAL PROJECT FOR NETWORK CLASS

# ----------------------------Necessary imports tkinter
from tkinter import *
import tkinter.messagebox as box
import tkinter.font as tkFont


# ----------------------------Imports for communication
import socket
import time

# setting the IP and ports
client_IP = socket.gethostname()
port = 7500

#Open a socket and connect the client to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_IP, port))
# 
individual_score = 0
questionsCount = 1
# ----------------------------Global constants
NAME_OF_THE_GAME = 'Friendly Feud'
WINDOW_SIZE = '500x500'

# ----------------------------Main window---------------------------------------
root = Tk()
root.title(NAME_OF_THE_GAME)
root.geometry(WINDOW_SIZE)

#backgroundImage = PhotoImage(file='../doc/app.jpg')

# ----- Store an integer as a picked choice identifier
v = IntVar()
a1 = StringVar()
# ----------------------------Global variables used by client.py
username = ''
current_question = StringVar()
a2 = StringVar()
a3 = StringVar()
a4 = StringVar()
questions_left = 2 # Show score when all questions are answered
scores = {'player1':0,'player2':0,'player3':0}
question_frame = Frame(root)

    
#receive the question/answer from server and update GUI variables
def get_question_from_server(num):
    """ Make a server request with the specified
        question number, num, and sets the client's global
        variables with the correct question content
    """
    global current_question, a1,a2,a3,a4

    #receive the question and choices in pieces
    client_socket.send(str(num).encode()) #send the question number
    
    current_question.set(str(client_socket.recv(1024).decode()))
    print('Question: ',current_question.get()) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    a1.set(str(client_socket.recv(1024).decode()))
    print('choice 1: ',a1.get()) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    a2.set(str(client_socket.recv(1024).decode()))
    print('choice 2: ',a2.get()) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    a3.set(client_socket.recv(1024).decode())
    print("choice 3: ", a3.get()) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())  # Stopped here

    a4.set(client_socket.recv(1024).decode())
    print('choice 4:',a4.get()) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    # Don't close here
    #client_socket.close()

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
    
def set_username():
    '''Get text from the entry and send it to the server'''
    global username
    username = uString.get()
    client_socket.send(username.encode())
    #time.sleep(10)
    client_socket.recv(1024).decode() #STATUS: CONNECTED
    print(username)
    usernameFrame.grid_forget()
    usernameFrame.destroy()

# Button to set username
button_get_username = Button(usernameFrame, text="Submit",
                          bg='white',
                          padx=5,
                          bd=0,
                          command=set_username).grid(row=0,column=3)

usernameFrame.grid(row=0,column=1)
# ------------------------------------------------------------------------------

def show_leaderboard():
    # -----------------------------------Leaderboard frame--------------------------

    leaderboard_frame = Frame(root)
    player_one_label = Label(leaderboard_frame,text='Player 1').grid(row=0, column=0)
    player_one_score = Label(leaderboard_frame,text=scores['player1']).grid(row=0, column=1)
    player_two_label = Label(leaderboard_frame,text='Player 2').grid(row=1, column=0)
    player_two_score = Label(leaderboard_frame,text=scores['player2']).grid(row=1, column=1)
    player_three_label = Label(leaderboard_frame,text='Player 3').grid(row=2, column=0)
    player_three_score = Label(leaderboard_frame,text=scores['player3']).grid(row=2, column=1)

    button_close_leaderboard = Button(leaderboard_frame, text="close",
                                  bg='white',
                                  padx=5,
                                  bd=0,
                                  command=lambda : leaderboard_frame.grid_forget()).grid(row=3,column=0)

    return leaderboard_frame

# ------------------------------------------------------------------------------
    
def show_current_question():
    '''Returns question frame with button handlers'''
    # -----------------------------------Question frame-----------------------------
    global question_frame, current_question, a1, a2, a3, a4
    question_label = Label(question_frame,textvariable=current_question,font=questionFontSize).grid(row=0,column=0)
    

    first = Radiobutton(question_frame,textvariable=a1,
                            variable=v,
                            indicatoron=0,
                            padx=20,
                            pady=2,
                            width=20,
                            bd=0,
                            height=4,
                            value=1).grid(row=1,column=1)



    second = Radiobutton(question_frame,textvariable=a2,
                             variable=v,
                             indicatoron=0,
                             padx=20,
                             width=20,
                             bd=0,
                             height=4,
                             value=2).grid(row=2,column=1)

    third = Radiobutton(question_frame,textvariable=a3,
                            variable=v,
                            indicatoron=0,
                            padx=20,
                            width=20,
                            bd=0,
                            height=4,
                            value=3).grid(row=3,column=1)

    fourth = Radiobutton(question_frame,textvariable=a4,
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
        global questions_left,individual_score,v,questionsCount
        
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
             # create a new frame with next question
             #questionsCount += 1
             #get_question_from_server(questionsCount)
             
             

        # Decide when to show score
        if questions_left == 0:
            question_frame.destroy()
            print('Show leaderboard here')
            show_leaderboard().grid(row=0,column=1)
            box.showinfo('Your score!', str(individual_score))
            # reset questions left for the next game
            questions_left = 2
            # close socket here
            client_socket.close()
        
    #-----------------------------Submit button
    submitButton = Button(question_frame, text="Submit",
                              bg='white',
                              padx=20,
                              width=20,
                              height=3,
                              bd=0,
                              command=sendToServer).grid(row=6,column=1)
    question_frame.grid(row=0, column=1)
    return question_frame


# ------------------------------------------------------------------------------


# ----------------------------Assign questions and anwers from the server ----
def startGame():
    get_question_from_server(questionsCount)
    # Show questions
    show_current_question()
    
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
