# server.py
# Network Programming Final Project

import socket
import _thread, time
import json
from random import randrange

#--------------------------------------------
# BACK-END STORAGE FOR QUESTIONS AND ANSWERS
#--------------------------------------------
QUESTIONS = {} 

with open ('questions.JSON') as inputfile:
    QUESTIONS = json.load(inputfile)
    inputfile.close()

client_number = 0 #to keep track of users that join the game
users_and_scores = {
    "user1" : {
        "username" : "Player 1",
        "score" : 0
    },
    "user2" : {
        "username" : "Player 2",
        "score" : 0
    },
    "user3" : {
        "username" : "Player 3",
        "score" : 0
    }
}

#-----------------------------------------------------------
#                        Server Settings
#------------------------------------------------------------
host = ''
port = 7500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
#Listen for sockets to begin accepting
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
    user_ID = 'user' + str(client_number) #store the User ID to avoid bugs when other users connect
    username = conn.recv(1024).decode()
    if not username:
        username = str(conn.address)    
    users_and_scores[user_ID]['username'] = username
    print(username + " connected to server.")
   

    #----------------------------------------------------
    #       THE GAME BEGINS BELOW (for client)
    #---------------------------------------------------

    client_score = 0

    for _i in range(5): #LOOP begins when the clien hits start game

        answer_key = send_question(conn) #send the first question
        conn.send("QUESTIONS SENT".encode())
        
        user_answer = conn.recv(1024).decode() #receive the answer
        conn.send("ANSWER RECEIVED".encode())

        if user_answer == answer_key: #check the answer
            client_score += 1
    
    print(username + ' finished the game.')
    print('score : ' + str(client_score))

    #Updating the scoreboard
    users_and_scores[user_ID]['score'] = client_score

    #SEND THE SCORE (may need to also send the userID to distinguish clients
    conn.send(str(client_score).encode())

    #send the scoreboard in str (json/dict format) ... client needs get_scoreboard()
    #send_scoreboard(conn)

    conn.close()

#-----------------------------------------------------------
#                 SERVER API TOOLS
#-----------------------------------------------------------

# Send question to client and return the answer
def send_question(conn):
        
    question_ID = 'question' + str(randrange(5)) #pick a random question 0-4
    category_ID = 'Category' + str(randrange(2)) 
    
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['question']) #send the question to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice1']) #send choice1 to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice2']) #send choice2 to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice3']) #send choice3 to the client
    send_data_to_client(conn, QUESTIONS[category_ID][question_ID]['choice4']) #send choice4 to the client
    
    return QUESTIONS[category_ID][question_ID]['answer']


#dumps scores/users in str and sends it to client
def send_scoreboard(conn):
    data = json.dumps(users_and_scores)
    conn.send(data.encode())


def send_data_to_client(conn, message):
    """ send the message from the server to the client
        inputs are the server connection, and the message
    """
    conn.send(message.encode())
    conn.recv(1024).decode() #STATUS: RECEIVED


#---------------------------------------------------------------------
#                               MAIN
#---------------------------------------------------------------------
def server_program3():
    """ The game server that will go online and open on port 7500,
        with multi-threading capabilities, the server is able to handle 
        hundreds of clients, but the limit for the game server is 3 clients.
    """
    print("Server is online...") #debugging purposes ... 
    global client_number

    while True:
        conn, address = server_socket.accept()
        print("Connection form: " + str(address) + ' at ' + str(now())) #debugging purposes ... 
        
        #IF SERVER REACHES MAX CAPACITY, RESET CLIENT_NUMBER AND #TODO: START NEW ROOM
        if client_number == 3: 
            client_number = 0 #reset ID
        else:
            client_number += 1
        
        #Starts a new thread for each client
        _thread.start_new(handleClient, (conn,))

if __name__=='__main__':
    server_program3()   
