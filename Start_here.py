from tkinter import Tk
import os
import time
import json
from Objects.Player import *                            # Player object
from Objects.Username import *                          # GUI username
from Objects.Leaderboard import *                       # GUI Leaderboard
from model.Question import *                            #
from server import *


# This is where the game can be controlled
def main():

    # This is root window
    root = Tk()
    root.geometry('480x600+20+20')

    # 1. Set username for the player
    p1 = Player()                               # Create player
    username = Username()                       # Create username frame
    p1.username = username.uString.get()        # Get username string
    # -------------------------------------------------------------------------

    # 2. Send username to the server
    server = Server()
    server.register_new_user(p1)                # Register player on the server

    # 3. Create quiz
    server.create_quiz()
    
    # 4. Start Quiz for player
    server.start_quiz(p1)

    # 5. Send leaderboard

    
    root.mainloop()                             # Show main window

if __name__ == '__main__':
    main()
