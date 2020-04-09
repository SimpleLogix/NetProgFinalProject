# This is a room for players
#from Player import *
class Room:
    # this tracks how many rooms were created
    room_number = 0
    # This set max players in the room
    room_capacity = 3
    
    def __init__(self):
        ''' Constructor '''
        self.room_id = Room.room_number # Each time room number increased by 1
        self.players = []
        self.quizes = []
        Room.room_number += 1

    def add_player(self,player):
        '''Add player to the room'''
        if len(self.players) < int(Room.room_capacity):
            self.players.append(player)
        else:
            print('Room is full')
    
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

    
