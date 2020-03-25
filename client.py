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

#GLOBAL VARIABLES
questions_number = 0 #keep track of the question # we are on
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

    while questions_number <= 10 :
       get_question_from_server()
       # this will loop all the way to the end of the question list
       # and send only the last one
       # I need to find a way to wait for the client to hit submit
       print (question) #debugging purposes ...


    
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
def get_question_from_server():
    client_socket.send(questions_number.encode()) #send the question number

    #receive the question and choices in pieces
    question = client_socket.recv(1024).decode()
    choice1 = client_socket.recv(1024).decode()
    choice2 = client_socket.recv(1024).decode()
    choice3 = client_socket.recv(1024).decode()
    choice4 = client_socket.recv(1024).decode()
    answer = client_socket.recv(1024).decode()
    #update the pointer for the next question
    questions_number += 1

if __name__=='__main__':
    client_program()