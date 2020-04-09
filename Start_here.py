from tkinter import Tk
import os
import time
import json
from Objects.Player import *
from Objects.Username import *
from Objects.Leaderboard import *
from Objects.Question import *


# This is where the game can be controlled
def main():
    root = Tk()
    root.geometry('480x600+20+20')

    p1 = Player() # Create player
    username = Username(p1) # Set players username
    question = Question(p1)

    root.mainloop()

if __name__ == '__main__':
    main()
