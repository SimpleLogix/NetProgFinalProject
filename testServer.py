# private server used for testing and debugging the client program
# WILL NOT BE A PART OF THE FINAL PROJECT


import socket
import _thread, time

host = ''
port = 7500

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen(2)

def now():
    return time.ctime(time.time())

def handleClient(conn):
    time.sleep(10)

    #receiving the usernames
    username = conn.recv(1024).decode()
    if not username:
        conn.send("Error! Must enter username".encode())
    else:
        welcomeMsg = "Welcome " + str(username) + ". Hit enter to begin the game"
        conn.send(welcomeMsg.encode())

    #--------------------------------------
    # THE GAME BEGINS BELOW #TODO: game auto starts after 5 sec.
    #---------------------------------------
    questions = ["Q1?","Q2?","Q3?"]
    user_answers = []

    for Q in questions:

        conn.send(Q.encode())
        reply = conn.recv(1024).decode()
        user_answers.append(reply) #saving the client answer
        print ("user " + username + " chose: " + str(reply))

    #conn.close()

def server_program3():
    
    print("Server is online...")
    
    while True:
        conn, address = server_socket.accept()
        print("Connection form: " + str(address) + ' at ' + str(now()))
        _thread.start_new(handleClient, (conn,))

if __name__=='__main__':
    server_program3()   
