This branch is based on master
# Client <-> Server multiple choice battlefield v0.5

## NOTICE: this is typical OOP approach. If we go this way, then we could do the replay or live score. But, it would be not easy to figured how to adjust the server and Question/Leaderboard/Player object to work together as before.
### This OOP approach, however, might be more adoptable for any further changes, if works as it expected.

### How to run the code?
1. Run server.py 
2.Run the Start_here.py
 
## Directory structure
1.images - images
2.Objects - classes for Player, Username, Leaderboard, Question
3.questions - JSON file with questions

## Classes

### Player
Player has sockets as the fields of the class, as well as the username, score and user_id

### Username
Username frame get player as an argument and can set player username

### Question
Question class get user as an argument and suppose to get question from the server, but something is not right.

### Leaderboard
Leaderboard is suppose to show player scores as before, but since we have Player object, which can hold scores, than we can somehow change the way the leaderbord would work.

