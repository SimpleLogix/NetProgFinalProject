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
        "answer" : "A1"
    },
    "question1" : {
        "question" : "Q2",
        "choice1" : "A1",
        "choice2" : "A2",
        "choice3" : "A3",
        "choice4" : "A4",
        "answer" : "A2"
    },
        "question2" : {
        "question" : "Q3",
        "choice1" : "A1",
        "choice2" : "A2",
        "choice3" : "A3",
        "choice4" : "A4",
        "answer" : "A3"
    },
        "question3" : {
        "question" : "Q4",
        "choice1" : "A1",
        "choice2" : "A2",
        "choice3" : "A3",
        "choice4" : "A4",
        "answer" : "A4"
    }
}


host = ''
port = 7500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(2)

def now():
    return time.ctime(time.time())

def handleClient(conn): #this is what shows up for each client
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
 
    question_number = 0
    str_question_number = conn.recv(1024).decode()
    question_ID = 'question' + str(str_question_number)
    
    conn.send(QUESTIONS[question_ID]['question'].encode())
    conn.recv(1024).decode() #STATUS: RECEIVED
    conn.send(QUESTIONS[question_ID]['choice1'].encode())
    conn.recv(1024).decode() #STATUS: RECEIVED
    conn.send(QUESTIONS[question_ID]['choice2'].encode())
    conn.recv(1024).decode() #STATUS: RECEIVED
    conn.send(QUESTIONS[question_ID]['choice3'].encode())
    conn.recv(1024).decode() #STATUS: RECEIVED
    conn.send(QUESTIONS[question_ID]['choice4'].encode())
    conn.recv(1024).decode() #STATUS: RECEIVED
    conn.send(QUESTIONS[question_ID]['answer'].encode())
    conn.recv(1024).decode() #STATUS: RECEIVED

    question_number += 1
    conn.send("Good bye!".encode())
    conn.close()

def server_program3():
    
    print("Server is online...") #debugging purposes ... 
    
    while True:
        conn, address = server_socket.accept()
        print("Connection form: " + str(address) + ' at ' + str(now())) #debugging purposes ... 
        _thread.start_new(handleClient, (conn,))

if __name__=='__main__':
    server_program3()   
