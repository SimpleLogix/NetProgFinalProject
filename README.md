# Client <-> Server multiple choice battlefield v0.4

### What to do with multithreading?
After some internet research, it appeared that we need to figured how the server will execute threads for each client.
The picture is as the following.

Client 1 --> q1 <-- Server thread for client 1 [q2,q3,q4,q5,q6,q7,q8,q9,q10] 
Question one sent, waiting for answer --> answer received --> execute thread (will sent next question and pause further execution)

Client 2 --> q2 <-- Server thread for client 2 [q3,q4,q5,q6,q7,q8,q9,q10] 

Client 3 --> q5 <-- Server thread for client 3 [q6,q7,q8,q9,q10] 

Each server thread should have a listener, which will trigger the execution of the next peace of code (assign next question for a client)

Since the way we do it now, seems like each client will receive the same question, and it assumes that all of the clients will answer questions simultaneously, which is not really happens.If we want the server to interact only with one client, then we can try to have a single user game. Otherwise, we have to come up with something that can manage multiple users independently.

### What about branches?
I've created a branch Alexperiments, where I am gonna do some wild implementations/variations of the master branch, without touching master branch.

### How to run the code?
1. Run the server.py
2. Run GUI.py

### About circular dependencies
We now have sort of an app architecture which is similar to MVC.Which is widely used for a mobile app development.
As before we wanted to import some function from client.py to the GUI.py to use them there. It is totally wrong and not necessary. Partially importing something from module A to module B, and something else from B to A is a circular dependecy. The python interpreter will know that and won't allow the program to be running. Instead we can import anything textual from GUI.py to client.py, including global variables. The module client.py will set values from the server(scores,usernames,questions,answers) into variables imported from GUI.py. The GUI.py job is primarily showing the interface and changing frames from start game state to leaderboard, showing scores and so forth. Since this small observation is based on the current code, later on it can be adjusted.

### Add images into GUI
The PhotoImage class can read GIF and PGM/PPM images from files:
photo = PhotoImage(file="image.gif")
photo = PhotoImage(file="lenna.pgm")

You can use a PhotoImage instance everywhere Tkinter accepts an image object. An example:
label = Label(image=photo)
label.image = photo # keep a reference!
label.pack()  or label.grid(row=0, column=0)

### Inserting question into GUI from the client.py
1. import the following variables from the GUI.py:
  username, current_question,a1,a2,a3,a4,questions_left,score
2. From client.py assign any required values to the imported variables in step 1
3. GUI.py will figure it out where to insert each value into labels
! Exception, any values stored as a list/dictionary/ might not be interpreted by GUI in a correct way

### We eventually moved to the known app architecture!
#### Model - server.py
This is typically a way the database schema looks like. In our case it is where the questions and answers are stored. As well as 
user's scores, etc. Any data that we use in the app.
#### View - GUI.py
This is where the user interface is designed. This part should be a slave of controller. Ideally we have all the functions which inserting values into the view, stored in the controller.
#### Controller - client.py
This is the part which connects Model with View. So, the controller will decide what user will see at the moment. The data from the model would be transfered to the View through the controller.


## What about running a server remotely?
### In this way we can figured how to test the server easier
### and be able to actually play this game.
- [ ] Explore a possibility of running the testServer.py file on the 
cloud hosting platforms, like AWS or something similar for free.

## Next steps...
So far we have managed to get the client to communicate with the server successfully and also been able to run and completely integrate the GUI with the client. The server

## What about GUI.py?
- [x] Basic User Interface with tkinter widgets
- [x] Show player's score
- [x] Start a new game
- [x] Exit the game
- [x] Show credits
- [ ] Game instruction 
- [ ] Visual styles(Colors, images, background?)
- [x] Transition to leaderbord
- [x] Add option to add username
- [x] Function returns selected choice
- [x] Function returns the username
- [ ] Update question frame function
---
    client functions:
- [x] Send answer to the server?
- [x] Get a question from the server?
- [ ] Get 4 distinct answers, one of which is correct and gives points
- [x] function send answer to server
- [x] function req a question from server (will be sent to GUI)
- [x] function req choices from server (sent to GUI)
- [ ] function req a score
- [x] fully integrated with GUI (client can communicate with server via GUI buttons)

## What about server.py?
- [x] Handle multiple clients?
- [x] Server-Client model using TCP
- [x] Store questions?
- [x] Store answers?
- [ ] Validate correctness of the answer provided by the clients?
- [x] Keep track of the usernames
- [ ] Keep track of user's scores
- [x] Sent how many questions in total




## Questions
- [x] Store questions as JSON file
- [x] Store questions as string variables / Dictionary
- [ ] Five categories, Twenty-Five questions
