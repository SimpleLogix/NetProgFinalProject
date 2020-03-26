# private server used for testing and debugging the client program
# WILL NOT BE A PART OF THE FINAL PROJECT

import socket
import _thread, time


#--------------------------------------------
# BACK-END STORAGE FOR QUESTIONS AND ANSWERS
# note: it is a dictionary now but can be put
# into a JSON file and parsed/loaded
#--------------------------------------------
QUESTIONS = {
    "question0" : {
        "question" : "Q1",
        "choice1" : "A1",
        "choice2" : "A2",
        "choice3" : "A3",
        "choice4" : "A4",
        "answer" : "1"
    },
    "question1" : {
        "question" : "Q2",
        "choice1" : "A1",
        "choice2" : "A2",
        "choice3" : "A3",
        "choice4" : "A4",
        "answer" : "2"
    },
        "question2" : {
        "question" : "Q3",
        "choice1" : "A1",
        "choice2" : "A2",
        "choice3" : "A3",
        "choice4" : "A4",
        "answer" : "3"
    },
        "question3" : {
        "question" : "Q4",
        "choice1" : "A1",
        "choice2" : "A2",
        "choice3" : "A3",
        "choice4" : "A4",
        "answer" : "4"
    }
}
QUESTION2 = {
    "Science" : {
        "question0" : {
            "question" : "wqewf???",
            "choice1" : "A!"
        },
        "question1" : {
            "question" : "???"
        }
    }
    
}


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
    #time.sleep(10)

    #receiving the usernames
    username = conn.recv(1024).decode()
    if not username:
        username = str(conn.address)
    
    print ("Welcome " + username)
    conn.send('STATUS: CONNECTED'.encode()) #send before we receive
    #--------------------------------------
    # THE GAME BEGINS BELOW #TODO: game auto starts after 5 sec.
    #---------------------------------------
    
    #Client sent the question number & made a request for the question contents
    str_question_number = conn.recv(1024).decode()
    question_ID = 'question' + str(str_question_number)
    
    send_data_to_client(conn, QUESTIONS[question_ID]['question']) #send the question to the client
    send_data_to_client(conn, QUESTIONS[question_ID]['choice1']) #send choice1 to the client
    send_data_to_client(conn, QUESTIONS[question_ID]['choice2']) #send choice2 to the client
    send_data_to_client(conn, QUESTIONS[question_ID]['choice3']) #send choice3 to the client
    send_data_to_client(conn, QUESTIONS[question_ID]['choice4']) #send choice4 to the client

    conn.send("Good bye!".encode())
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
