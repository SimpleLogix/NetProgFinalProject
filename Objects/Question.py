#Question frame
from tkinter.ttk import Frame
from tkinter import Tk, PhotoImage, StringVar,IntVar,Canvas
from tkinter.ttk import Frame, Button, Label, Entry, Progressbar, Radiobutton
from tkinter import messagebox as mbox

# Shows scores for players
class Question(Frame):
    '''
        Question frame get arguments for each question
        Player is passed to sent question to connected
        Players
    '''
    def __init__(self,player):
        self.v = IntVar()
        self.question = StringVar()
        self.a1 = StringVar()
        self.a2 = StringVar()
        self.a3 = StringVar()
        self.a4 = StringVar()
        self.player = player
        self.questionsLeft = 10
        super().__init__()
        self.initMain()

    def get_question_from_server(self):
        '''Set next question'''

        #receive the question and choices in pieces
        
        self.question.set(str(self.player.client_socket.recv(1024).decode()))
        self.player.client_socket.send('STATUS: RECEIVED'.encode())

        self.a1.set(str(self.player.client_socket.recv(1024).decode()))
        self.player.client_socket.send('STATUS: RECEIVED'.encode())

        self.a2.set(str(self.player.client_socket.recv(1024).decode()))
        self.player.client_socket.send('STATUS: RECEIVED'.encode())

        self.a3.set(str(self.player.client_socket.recv(1024).decode()))
        self.player.client_socket.send('STATUS: RECEIVED'.encode())  

        self.a4.set(str(self.player.client_socket.recv(1024).decode()))
        self.player.client_socket.send('STATUS: RECEIVED'.encode())
       
            
    def initMain(self):
        '''Initialize the start game window'''
        self.master.title('Friendly Feud')
        self.pack()
        # Add content of the questions

        w = Canvas(self,height=480,width=480)
        w.pack(expand=True, fill='both')
        # Create an image
        w.image = PhotoImage(file="images/question_active.gif")
        w.create_image(0,0, image=w.image,anchor='nw')

    
        question_label = Label(self,textvariable=self.question).pack()
    

        first = Radiobutton(self,textvariable=self.a1,
                            variable=self.v,
                            width=20,
                            value=1).pack()



        second = Radiobutton(self,textvariable=self.a2,
                             variable=self.v,
                             width=20,
                             value=2).pack()

        third = Radiobutton(self,textvariable=self.a3,
                            variable=self.v,
                            width=20,
                            value=3).pack()

        fourth = Radiobutton(self,textvariable=self.a4,
                             variable=self.v,
                             width=20,
                             value=4).pack()

        #-----------------------------Submit button
        submitButton = Button(self, text="Submit",
                                  command=self.sendToServer).pack()


    # Submit button handler
    # Send the value from the checkbox to the server
    def sendToServer(self):
        '''This function sends an answer to the server'''
        # Case when no answer given
        if self.v.get() == 0:
            mbox.showinfo('Oops...','Have to pick one of the provided answers')

        self.questionsLeft -= 1
        
        # Decide when to show score
        if self.questionsLeft == 0:
            self.pack_forget()
          
            #sending to server
            self.player.client_socket.recv(1024).decode() 
            self.player.client_socket.send(str(v.get()).encode()) #send the answer to server
            self.player.client_socket.recv(1024).decode() 
            self.player.client_socket.send('REQUESTING CLIENT SCORE'.encode())
            #player.group_score = client_socket.recv(1024).decode() #THIS IS WHERE THE END OF COMMUNICATION IS
            
            self.data = json.loads(group_score)

            #------set scores from data
            print('Show leaderboard here')
            # SET player scores from the leaderboard's server data
            
            p1 = data['user1']['score']
            p2 = data['user2']['score']
            p3 = data['user3']['score']

            # SET player's usernames
            one = data['user1']['username']
            two = data['user2']['username']
            three = data['user3']['username']
            
            # Create leaderboard, pass necessary players info
            leaderboard = Leaderboard(one,two,three,p1,p2,p3)
            
            # reset questions left for the next game
            self.questionsLeft = 10
            
        # Answer is given
        else:
            print(self.v.get())# Will print which number was selected
            self.player.client_socket.recv(1024).decode() 
            self.player.client_socket.send(str(self.v.get()).encode()) #send the answer to server
            self.player.client_socket.recv(1024).decode() 
            
            # This would be where we can add the ability to update score in real time
            # AKA let client know if they got the question right/wrong

            # create a new frame with next question
            self.v.set(0) # reset the selection for the next question

    
