# private server used for testing and debugging the client program
# WILL NOT BE A PART OF THE FINAL PROJECT

import socket
import _thread, time
import json, os
from random import randrange

#--------------------------------------------
# BACK-END STORAGE FOR QUESTIONS AND ANSWERS
#--------------------------------------------
QUESTIONS = {} 

with open ('questions.json') as inputfile:
    QUESTIONS = json.load(inputfile)
    inputfile.close()

connected_users = []

user_scores = {
    "player1" : 0,
    "player2" : 0,
    "player3" : 0
}

#-----------------------------------------------------------
#                        Server Settings
#------------------------------------------------------------
host = ''
port = 7500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(2)

def now():
    """ Returns the current time in string
    """
    return time.ctime(time.time())

def handleClient(conn): #this is what shows up for each client
    """ This is how the server will handle each client that connects
        This function will run once for every client but may not all be synced
        **figure out a way to have the client wait if the other clients are still playing
    """

    #receiving the usernames
    username = conn.recv(1024).decode()
    if not username:
        username = str(conn.address)    
    connected_users.append(username)

    print ("Welcome " + username)
    conn.send('STATUS: CONNECTED'.encode()) #send before we receive
    #--------------------------------------
    # THE GAME BEGINS BELOW #TODO: game auto starts after 5 sec.
    #---------------------------------------
    
    #Client sent the question number & made a request for the question contents
    str_question_number = conn.recv(1024).decode()
    question_ID = 'question' + str(str_question_number)
    #category_ID = 'Category' + str(randrange(5)) #pick a random category 0-4
    category_ID = 'Category0'
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['question']) #send the question to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice1']) #send choice1 to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice2']) #send choice2 to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice3']) #send choice3 to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice4']) #send choice4 to the client

    conn.send("Good bye!".encode())
    connected_users.remove(username)
    conn.close()

def server_program3():
    """ The game server that will go online and open on port 7500,
        with multi-threading capabilities, the server is able to handle 
        hundreds of clients, but the limit for the game server is 3 clients.
    """
    print("Server is online...") #debugging purposes ... 
    
    while True:
        conn, address = server_socket.accept()
        print("Connection form: " + str(address) + ' at ' + str(now())) #debugging purposes ... 
        _thread.start_new(handleClient, (conn,))

def send_data_to_client(conn, message):
    """ send the message from the server to the client
        inputs are the server connection, and the message
    """
    conn.send(message.encode())
    conn.recv(1024).decode() #STATUS: RECEIVED

if __name__=='__main__':
    server_program3()   
