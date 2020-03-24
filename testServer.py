# private server used for testing and debugging the client program
# WILL NOT BE A PART OF THE FINAL PROJECT


import socket
import _thread, time

host = ''
port = 7500

server_socket = socket.socket()
server_socket.bind((host,port))
server_socket.listen(2)

def now():
    return time.ctime(time.time())

def handleClient(conn):
    time.sleep(10)

    #receiving the usernames
    data = conn.recv(1024).decode()
    if not data:
        conn.send("Error! Must enter username".encode())
    else:
        welcomeMsg = "Welcome " + str(data) + ". Type 'start' to begin the game"
        conn.send(welcomeMsg.encode())

    #wait for user to start the game
    data = conn.recv(1024).decode()
    if data.strip() == 'start':
        conn.send("OK".encode())
    else:
        data = conn.recv(1024).decode()
    #conn.close()

def server_program3():
    while True:
        conn, address = server_socket.accept()
        print("Connection form: " + str(address) + ' at ' + str(now()))
        _thread.start_new(handleClient, (conn,))

if __name__=='__main__':
    server_program3()   