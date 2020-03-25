# Client <-> Server multiple choice battlefield v0.3

### How to run the code?
1. Run the testServer.py
2. Run GUI.py

Now we have a little bit more complicated program structure.
GUI.py importing client.py module
When we run GUI.py the client.py code is able to establish 
a connection to the server

I figured that this observation is helpful. Meaning that we already have
our client.py and GUI.py integrated together.

The testServer.py will be running separately.

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
- [ ] Store questions?
- [ ] Store answers?
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

## Questions
- [ ] Store questions as text files
- [ ] Store question as JSON file

***note: we should decide if we will use UDP/TCP and also display strings from client.py & server.py on the GUI

