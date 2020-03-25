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

#GLOBAL VARIABLES
question = '' #The current displayed question
answer = '' #The answer to the current question
choice1 = '' 
choice2 = ''
choice3 = ''
choice4 = ''
scores = [] #The scores of all the players

# setting the IP and ports
client_IP = socket.gethostname()
port = 7500

#Open a socket and connect the client to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((client_IP, port))

def client_program():
   
    #sending the username to the server
    user = get_username()
    client_socket.send(user.encode())
    #time.sleep(10)
    client_socket.recv(1024).decode() #STATUS: CONNECTED
    #--------------------------------------------
    #        THE GAME BEGINS BELOW  
    # it is the client's job to request questions
    # from the server and update the local variables
    # with such. 
    # When the client submits their answer, another
    # request will be made to the server for the 
    # next question.
    #--------------------------------------------

    #requesting A question (index 0-9)
    questions_number = 0 #keep track of the question # we are on
    
    
    get_question_from_server(questions_number)


    # TODO: turn dictionary into JSON file
    # TODO: LOOP through all of the questions
    # TODO: Successfully communicate and integrate with the GUI
    




    
    #client_socket.close() #uncomment to close the connection

#get the selected answer from GUI (temporary! import from GUI)
def get_answer():
    return 0

#get username from GUI (temporary! import from GUI)
def get_username():
    return "user"

#sends the question to the GUI
def request_question():
    return question

#sends the choices (as a list) to the GUI
def request_choices():
    choices = [choice1, choice2, choice3, choice4]
    return choices

#sends the scores to the GUI
def request_scores():
    return scores

#receive the question/answer from server
def get_question_from_server(num):
    str_question_number = str(num)
    client_socket.send(str_question_number.encode()) #send the question number
    #receive the question and choices in pieces
    global question 
    question = client_socket.recv(1024).decode()
    print("question: " + question) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())
    global choice1 
    choice1 = client_socket.recv(1024).decode()
    print("choice 1: " + choice1) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())
    global choice2 
    choice2 = client_socket.recv(1024).decode()
    print("choice 2: " + choice2) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())
    global choice3 
    choice3 = client_socket.recv(1024).decode()
    print("choice 3: " + choice3) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())
    global choice4 
    choice4 = client_socket.recv(1024).decode()
    print("choice 4: " + choice4) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())
    global answer
    answer = client_socket.recv(1024).decode()
    print("answer: " + answer) # FOR Debugging Purposes ...
    client_socket.send('STATUS: RECEIVED'.encode())
    
    #update the pointer for the next question
    num += 1

if __name__=='__main__':
    client_program()