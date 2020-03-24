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

def client_program():
    
    
    # setting the IP and ports
    clientIP = socket.gethostname()
    serverIP = '127.0.0.1'
    port = 7500

    #Open a socket and connect the client to the server
    client_socket = socket.socket()
    client_socket.connect((serverIP, port))
    
    #sending the username
    user = input('Enter username: ')
    client_socket.send(user.encode())

    #now we wait for the client to start the game (by typing 'start')
    data = client_socket.recv(1024).decode()
    print('From server: ' + data )
    
    message = input(' -> ')                     #TODO: figure a way to wait for user to type 'start' 
    client_socket.send(message.encode())
    serverResponse = client_socket.recv(1024).decode()
    while serverResponse != 'OK':    
        message = input(' -> ')
        client_socket.send(message.encode())
        serverResponse = client_socket.recv(1024).decode()
    #client_socket.close()

def send_answer():
    0



if __name__=='__main__':
    client_program()