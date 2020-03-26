# Client <-> Server multiple choice battlefield v0.3

### How to run the code?
1. Run the testServer.py
2. Run GUI.py

### About circular dependencies
We now have sort of an app architecture which is similar to MVC.Which is widely used for a mobile app development.
As before we wanted to import some function from client.py to the GUI.py to use them there. It is totally wrong and not necessary. Partially importing something from module A to module B, and something else from B to A is a circular dependecy. The python interpreter will know that and won't allow the program to be running. Instead we can import anything textual from GUI.py to client.py, including global variables. The module client.py will set values from the server(scores,usernames,questions,answers) into variables imported from GUI.py. The GUI.py job is primarily showing the interface and changing frames from start game state to leaderboard, showing scores and so forth. Since this small observation is based on the current code, later on it can be adjusted.

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


## What about GUI.py?
- [x] Basic User Interface with tkinter widgets
- [x] Show player's score
- [x] Start a new game
- [x] Exit the game
- [x] Show credits
- [ ] Game instruction 
- [ ] Visual styles(Colors, images, background?)
- [ ] Transition to leaderbord
- [ ] Add option to add username
- [ ] Function returns selected choice
- [ ] Function returns the username

## What about server.py?
- [ ] Handle multiple clients?
- [x] Store questions?
- [x] Store answers?
- [ ] Validate correctness of the answer provided by the clients?
- [ ] Keep track of the usernames
- [ ] Keep track of user's scores
- [ ] Sent how many questions in total

## What about client.py?
- [x] Send answer to the server?
- [x] Get a question from the server?
- [ ] Get 4 distinct answers, one of which is correct and gives points
- [x] function send answer to server
- [x] function req a question from server (will be sent to GUI)
- [x] function req choices from server (sent to GUI)
- [ ] function req a score
- [ ] fully integrated with GUI (client can communicate with server via GUI buttons)

## Questions
- [ ] Store questions as text files
- [ ] Store questions as JSON file
- [ ] Store questions as string variables / Dictionary

***note: we should decide if we will use UDP/TCP and also display strings from client.py & server.py on the GUI

