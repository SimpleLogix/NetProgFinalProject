import socket
# This is a generator of player's unique identifiers
import uuid 


# This is a player
class Player:
    count = 0                                               # Keep track of the instances
    
    def __init__(self):                                     
        Player.count += 1
        self.port = 7500

        # ------------------------The channel of communication with the server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_ip = socket.gethostname()
        self.connect = self.client_socket.connect((self.client_ip, self.port))
        # -------------------------------------------------------------------
        self.username = ''
        self.score = '0'
        self.user_id = uuid.uuid1() # Create unique client ID
        
    def register_on_server(self):               # Handler for user registration on the server
        '''Register on the server'''
        self.send_to_server(self.user_id.int)   # send UUID
        self.receive_from_server()              # receive reply
        self.disconnect()                       # close the connection

    def request_game_start(self):
        '''Start game request'''
        # Receive question from the server
        self.receive_from_server()

        # Send answer
        self.send_to_server('answer')

        # Receive score here
        self.score += self.receive_from_server()
        
        
    def disconnect(self):
        '''Close connection'''
        self.client_socket.close()
        
    def send_to_server(self,data):
        '''Send data to the server'''
        return self.client_socket.send(str(data).encode())
        
    def receive_from_server(self):
        '''Receive data from the server'''
        return self.client_socket.recv(1024).decode()

    def __str__(self):
        '''String method for the object'''
        return '(user_id='    +  str(self.user_id)   + '\n' +\
               'username='   +  str(self.username)  + '\n' +\
               'score='      +  str(self.score)     + '\n' +\
               'client_ip='  +  str(self.client_ip) + '\n' +\
               'client_port='+  str(self.port)      + '\n' +\
               ')'

               
if __name__ == '__main__':
    '''Test this module'''
    p1 = Player()
    print(str(p1))
    # Register on the server
    #p1.register_on_server()
    
    
   
