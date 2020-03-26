# -*- coding: utf-8 -*-
"""
Created on Mon Mar  23 16:30:31 2020

-------------------------------------------------------------
The client program which establishes connection to the game server 
and allows users to join a multiplayer room to compete against
each other. The client acts as the middleman between the GUI and 
the server, requesting data from the server and displaying it
for the user in the GUI.
-------------------------------------------------------------

@author: harkousw
"""

import socket
import time
# imports from GUI
<<<<<<< HEAD:client.py
from GUI import v,username, current_question, a1, a2, a3, a4, show_current_question
=======
from GUI import v,username, current_question, a1, a2, a3, a4, scores

>>>>>>> a292b96a9f13c28174f8919900cafd73bcf6269c:Friendly Feud/client.py

#GLOBAL VARIABLES (USED ONLY WITHIN client.py)
question_number = 0 #The question number (index 0-9)


# setting the IP and ports
client_IP = socket.gethostname()
port = 7500

#Open a socket and connect the client to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_IP, port))

def client_program():
    """ Client program to connect to server and 
        open communication between user and game server
    """
    #sending the username to the server
    user = get_username()
    client_socket.send(user.encode())
    #time.sleep(10)
    client_socket.recv(1024).decode() #STATUS: CONNECTED
    #--------------------------------------------------------
    #                 THE GAME BEGINS BELOW  
    #-------------------------------------------------------

    # ask for first question
    get_question_from_server(0) 

    # 3/26/20 
    #    couple of options at this point...
    # 1) we can request 10 random questions and store them on the client side
    #    make reference to them and update the GUI to those through a loop.
    # ----------------------------------------------------
    # 2) we can make a request for one question at a time, and update
    #    the variables once when the game is initialized, and again each
    #    time the user hits submit.
  

    # TODO: turn dictionary into JSON file
    # TODO: LOOP through all of the questions
 
    #client_socket.close() #uncomment to close the connection

#[X] Answer is imported from GUI's radiobutton
def get_answer():
    '''return an integer which represents
       which choice was selected(1,2,3,4) 
    '''
    return v.get()

#[X] Username is imported from GUI's entry
def get_username():
    '''get username from userNameEntry'''
    return username


#receive the question/answer from server and update GUI variables
def get_question_from_server(num):
    """ Make a server request with the specified
        question number, num, and sets the client's global
        variables with the correct question content
    """
    global current_question, a1, a2, a3, a4

    #receive the question and choices in pieces
    client_socket.send(str(num).encode()) #send the question number
    current_question = client_socket.recv(1024).decode()
    print("question: " + current_question) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    a1 = client_socket.recv(1024).decode()
    print("choice 1: " + a1) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    a2 = client_socket.recv(1024).decode()
    print("choice 2: " + a2) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    a3 = client_socket.recv(1024).decode()
    print("choice 3: " + a3) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    a4 = client_socket.recv(1024).decode()
    print("choice 4: " + a4) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())

    show_current_question(current_question, a1, a2, a3, a4)
    
#Request the leaderboard scores from server
def get_scores_from_server():
    pass

if __name__=='__main__':
    client_program()
