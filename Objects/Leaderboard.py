from tkinter import Tk, PhotoImage, StringVar,IntVar,Canvas
from tkinter.ttk import Frame, Button, Label, Entry, Progressbar, Radiobutton
from tkinter import messagebox as mbox
# Shows scores for players
class Leaderboard(Frame):
    '''Leaderboard frame is initially hidden'''
    def __init__(self,p1,p2,p3,s1,s2,s3):
        super().__init__()
        self.initMain(p1,p2,p3,s1,s2,s3)

    def close_leaderboard(self):
        '''Destroy the window'''
        self.destroy()
            
    def initMain(self,p1,p2,p3,s1,s2,s3):
        '''Initialize the start game window'''
        self.master.title('Leaderboard')
        self.pack()

        leaderboard_scores = Label(self, text='SCORES').grid(row=0,column=0,columnspan=3)
        
        player_one_label = Label(self,text=p1).grid(row=1,
                                                    column=0,
                                                    padx=15,
                                                    pady=15)
        player_one_score = Label(self,text=s1).grid(row=1,
                                                    column=1,
                                                    padx=15,
                                                    pady=15)
        player_two_label = Label(self,text=p2).grid(row=2,
                                                    column=0,
                                                    padx=15,
                                                    pady=15)
        player_two_score = Label(self,text=s2).grid(row=2,
                                                    column=1,
                                                    padx=15,
                                                    pady=15)
        player_three_label = Label(self,text=p3).grid(row=3,
                                                      column=0,
                                                      padx=15,
                                                      pady=15)
        
        player_three_score = Label(self,text=s3).grid(row=3,
                                                      column=1,
                                                      padx=15,
                                                      pady=15)

        # Exit the program
        button_close_leaderboard = Button(self, text="close",
                                      command=self.close_leaderboard).grid(row=4,column=0,columnspan=3)

