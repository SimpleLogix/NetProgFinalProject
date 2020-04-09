# server.py
# Network Programming Final Project

import socket
import _thread, time
import json
from random import randrange
from model.Player import *
from model.Room import *
from model.Quiz import *


class Server:
    
    '''Server Object for interactions with the client through sockets'''
    def __init__(self):
        # All the questions on the server
        self.QUESTIONS = {}
        # load question as soon as the server is created
        self.source_from_JSON()
        #-----------------------------------------------------------
        #                        Server Settings
        #------------------------------------------------------------
        self.host = ''
        self.port = 7500
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host,self.port))
        
        #@TODO:  Register players in the room
        self.rooms = Room() # One room
        self.registered_users = []
        self.limit = 3 # how many registrations are allowed

    # This handles user's registration
    def register_new_user(self,player):
        '''Receives user's ID and add to the Room'''
        print('Connected ')
        print(str(player))

        # Receive player's UUID
        message = self.server_accept(player)
        self.server_send(player,message)

        # Add to the list of registered users
        self.registered_users.append(message)
        print(str(self.server_accept(player)))

        # Send to the client his UUID
        print('Registered successfully')
        self.server_send(player,'Registered ')

    def create_leaderboard(self):
        '''Create a leaderboard based on scores from the registered_users'''
        pass

    def create_quiz(self,player):
        '''Create Quiz with questions'''
        quiz = Quiz()
        # Create 10 empty questions
        q.init_quiz_questions()

        # Insert questions from server's database
        
        q.fill_questions(QUESTIONS[category_ID][question_ID]['question'],
                         QUESTIONS[category_ID][question_ID]['choice1'],
                         QUESTIONS[category_ID][question_ID]['choice2'],
                         QUESTIONS[category_ID][question_ID]['choice3'],
                         QUESTIONS[category_ID][question_ID]['choice4'],
                         QUESTIONS[category_ID][question_ID]['answer'])

        # How many questions left
        questions_left = len(q.Questions)
        # Keep communication while questions left
        while questions_left > 0:
            # Send question to the client
            server_send(player,q.Questions[questions_left])
            # Receive answer from the client
            answer = player.server_accept()
            # set answer for the given Question object
            q.Questions[questions_left].received = answer
            # compare to correct answer
            if q.Questions[questions_left].received == q.Questions[questions_left].correct: #check the answer in th question
                # Identify the client by UUID
                # Send to the correct Player Object
                # Client should append to the score field
                server.send(player,1)
            else:
                server.send(player,0)
                
            # send acknowledgment to the client if the answer is correct
            
            # Show how many questions left
            questions_left -= 1

        player.close() # close the connection with the payer

           
    # -------------------------------------------------
    # Server's main method for client handlers
    # -------------------------------------------------
    def start_server(self):
        '''Start the server'''
        self.server_socket.listen(2)

        print('Listening...')
        # loop to await for incomming connections
        while True:
            conn, address = self.server_socket.accept()

            # Start the game handler
            if len(self.registered_users) == 3:
                print('Start the game')
                # Handle connected user in 
                _thread.start_new(self.create_quiz, (conn, ))
                
            # Registration handler
            elif len(self.registered_users) < 4:
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
