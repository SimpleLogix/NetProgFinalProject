# This is a room for players
from Player import *
from Quiz import *

class Room:
    
    room_number = 0                             # this tracks how many rooms were created
    
    def __init__(self):
        ''' Constructor '''
        Room.room_number += 1                   # increment room number
        self.room_id = Room.room_number         # each time room number increased by 1
        self.players = []                       # how many players in the room
        self.quiz = Quiz()                      # create one quiz for the room     
    
    #----------------------------------------------------------------
    #                   Use methods for any external calls
    #----------------------------------------------------------------
    def add_player(self,player):
        '''Add player to the room'''
        if len(self.players) < int(Room.room_capacity):
            self.players.append(player)
        else:
            print('Room is full')
            return -1                           # indicates that the room is full
    
    def __str__(self):
        '''String method for the object'''
        return '(room_id='    +  str(self.room_id)   + '\n' +\
               'total_player= ' + str(len(self.players)) + ')'

if __name__ == '__main__':
    '''Test this module'''
    r1 = Room()
    print(str(r1))

    print('Add player\n')
    p1 = Player()
    p2= Player()
    p3 = Player()
    p4 = Player()
    
    r1.add_player(p1)
    r1.add_player(p2)
    r1.add_player(p3)
    print(str(r1))
    r1.add_player(p4)
    r1.add_player(p3)
    r1.add_player(p2)

    
