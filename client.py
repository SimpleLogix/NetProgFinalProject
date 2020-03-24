# -*- coding: utf-8 -*-
"""
Created on Mon Mar  23 16:30:31 2020

-------------------------------------------------------------
Some parts of the code are copied from the clientProgram code 
from class will be manipulating to our application standards
-------------------------------------------------------------

@author: harkousw
"""

import socket

# setting the IP and ports
clientIP = socket.gethostname()
port = 7500

#Open a socket and connect the client to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((clientIP, port))

def client_program():
   
 
    #sending the username
    user = input('Enter username: ')
    client_socket.send(user.encode())

    #now we wait for the client to start the game (by hitting 'Enter')
    data = client_socket.recv(1024).decode()
    print('From server: ' + data )
    
    message = input(' -> ')                     
    client_socket.send(message.encode())
    
    #--------------------------------------
    # THE GAME BEGINS BELOW #TODO: game auto starts after 5 sec.
    #---------------------------------------
    gameStatus = 'Running'

    for _i in range(3): #testing with 3 questions for now
        question = client_socket.recv(1024).decode()
        print(question)
        answer = input('choose A | B | C | D : ')
        client_socket.send(answer.encode())

    print ("Thank you for playing!\n" + "Goodbye!")
    client_socket.close()

def send_answer():
    0



if __name__=='__main__':
    client_program()