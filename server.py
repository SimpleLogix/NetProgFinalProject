# server.py
import socket
import _thread, time
import json
from random import randrange
from model.Player import *
from model.Room import *
from model.Quiz import *

class Server:
    '''Server only waits for the incoming user to register and add to the rooms'''

    def __init__(self):
        #-----------------------------------------------------------
        #                        Server Settings
        #------------------------------------------------------------
        self.host = ''
        self.port = 7500
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host,self.port))
        #------------------------------------------------------------
        #                        Manage rooms
        #------------------------------------------------------------
        self.room_num = 0
        self.rooms = []                                                 # hold rooms 
        self.rooms.append(Room())                                       # create first room
        #------------------------------------------------------------
        #                       Manage questions
        #------------------------------------------------------------
        self.QUESTIONS = {}
        self.source_from_JSON()                                         # load questions

    # This handles user's registration
    def register_new_user(self,player):
        '''Receives user's ID and add to the Room'''
        print('Connected ')
        print(str(player))
  
        message = self.server_accept(player)                # Receive player's UUID
        self.server_send(player,message)                    # Send player a message

        if self.rooms[self.room_num].add_player(player):    # Add player to the room
            self.rooms[self.room_num].add_player(player)    # Added
        else:                                               # Create another room
            self.rooms.append(Room)                         # Room created
            self.room_num += 1                              # Indicate next room number
            self.rooms[self.room_num].add_player(player)    # Add player to the new room

        print('Registered successfully')                    # Player registered
        self.server_send(player,'Registered ')              

    def create_leaderboard(self):
        '''Create a leaderboard based on scores from the registered_users'''
        pass
    
    def start_quiz(self,player):
        '''Start quiz'''
    
        questions_left = len(self.rooms[room_num.quiz.questions])       # How many questions left from the quiz
        
        while questions_left > 0:                                       # Keep communication while questions left
         
            server_send(player,self.rooms[room_num.quiz.questions[questions_left]]) # Send question number n - 1
            
            answer = server_accept(player)                              # Receive answer from the client
            
            player_answer = self.rooms[room_num.quiz.questions[questions_left].received]
            player_answer = answer                                      # set answer for the given Question object
            correct_answer = self.rooms[room_num.quiz.questions[questions_left].correct]           
            
            if player_answer == correct_answer:                         # check the answer in the question
                server.send(player,1)                                   # send one point to the player
            else:
                server.send(player,0)                                   # send 0 points
            
            # Live score feature  
            # @TODO: send acknowledgment to the client if the answer is correct
            questions_left -= 1                             # Show how many questions left
        player.close()                                      # close the connection with the palyer

    def create_quiz(self):
        '''Create Quiz with questions for each room'''
        quiz = self.rooms[room_num].quiz                    # Quiz for each room
        quiz.init_quiz_questions()                          # Create 10 empty questions

        category_ID = random.randrange(5)                   # random category
        question_ID = random.randrange(5)                   # random question number

        # Insert questions from server's database
        quiz.fill_questions(QUESTIONS[category_ID][question_ID]['question'],
                         QUESTIONS[category_ID][question_ID]['choice1'],
                         QUESTIONS[category_ID][question_ID]['choice2'],
                         QUESTIONS[category_ID][question_ID]['choice3'],
                         QUESTIONS[category_ID][question_ID]['choice4'],
                         QUESTIONS[category_ID][question_ID]['answer'])

    # -------------------------------------------------
    # Server's main method for user's registration
    # -------------------------------------------------
    def start_server(self):
        '''Start the server'''
        self.server_socket.listen(2)

        print('Listening...')
        # loop to await for incomming connections
        while True:
            conn, address = self.server_socket.accept()

            # Handle connected user in 
            _thread.start_new(self.register_new_user, (conn, ))
    # ---------------------------------------------------
    
    def server_accept(self,conn):
        '''Server receives something from the client'''
        return conn.recv(1024).decode()

    def server_send(self,conn,payload):
        '''Server sends something'''
        return conn.send(str(payload).encode())
        
    def source_from_JSON(self):
        '''Loads questions from the JSON into server's QUESTIONS field'''
        with open ('questions/questions.JSON') as inputfile:
            self.QUESTIONS = json.load(inputfile)
            inputfile.close()


if __name__=='__main__':
     #Create a server
     server = Server()
     
     # Start server 
     #server.start_server()
