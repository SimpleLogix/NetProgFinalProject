import socket
from tkinter import StringVar

# This is a player
class Player():

    def __init__(self):
        self.port = 7500
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_ip = socket.gethostname()
        self.connect = self.client_socket.connect((self.client_ip, self.port))
        self.username = StringVar()
        self.score = StringVar()
        self.user_id = 0
