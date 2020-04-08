from tkinter import Tk, PhotoImage, StringVar,IntVar,Canvas
from tkinter.ttk import Frame, Button, Label, Entry, Progressbar, Radiobutton
from tkinter import messagebox as mbox


# Username frame
class Username(Frame):
    '''
        Represents a single frame
        Pass user to determine where to set name
    '''

    def __init__(self,player):
        self.uString = StringVar()
        self.player = player
        super().__init__()
        self.initMain()

    def initMain(self):
        '''Initialize the start game window'''
        self.master.title('Friendly Feud')
        self.pack()

        w = Canvas(self,height=480,width=480)
        w.pack(expand=True, fill='both')
        # Create an image
        w.image = PhotoImage(file="images/giphy.gif")
        w.create_image(0,0, image=w.image,anchor='nw')
        
                
        # create username
        label_username = Label(self,text='Username:')
        label_username.pack()
        
        # Entry to ask for a username
        userNameEntry = Entry(self,textvariable=self.uString,width=20)
        userNameEntry.pack()

        # Button to set username
        button_get_username = Button(self,
                                     text="Submit",
                                     command=self.set_username).pack()

    def set_username(self):
        '''Get text from the entry and send it to the server'''
        self.username = self.uString.get()
        self.player.client_socket.send(self.username.encode())
        # This line freezing the UI
        #time.sleep(10)
        print('Username is : ', self.username)
        self.grid_forget()
        self.destroy()
        
        
