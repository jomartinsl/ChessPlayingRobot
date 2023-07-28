# Chess playing robot

This project's is about getting a UR5e robotarm to play chess against you. We have a DGT-board and a UR5e robot to disposition.
The code for this project is divided in two. We have the chess-python code and ur5e-code. 

The ```MainTestFile.py``` is where the program runs from. This is where you call the ```URClass.py``` and ```MainforChessengine.py``` and get the program to run.

Under the different classes is beeing described:

### ```MainTestFile```
Start's the game


### ```URClass.py```
This class, ```URClass.py``` is used for the UR5-e robot arm. You controll the starting position, which is where it's ready to make the next move, and the code for all the 64-squares at the chessboard. 
The robot is controlled with TCP, tool-centre-point, to every position. The 'moverob()' function is where you want to put the start-square and the end-square when the robot is making a move. Example Nc3 -> from-square = b1, to-square = c3. B1 and c3 will be put in as parametre in the function. 'moverob('b1', 'c3'). The designations are something that repeats itself, for example 'Nc3' is a "san" value and 'b1c3' is a "uci" value which is important to understand the code.

### ```MainforChessengine.py```
This is where the chessengine talks with the DGT board. The move that is been played will be sent to this class and the engine will make the best or worst move in return. 

### ```ChessEngine.py```
This the the part you dont touch. This is the chessengine that calculate the best move, depends on the depth you are playing on. High depth makes the engine better, but also takes longer time to answer with a good move.

### ```testChess.py```
This class is mainly used for converting the move that has been made, into san-value. For instance if you move the pawn from e2 to e4 it will return the san-value 'e4'. When the dgt-board detects a change in the pattern it will scan the current state and save the previous state. The only task for this class is to return one value which is the san-value.

### ```robotiq_gripper_control.py```
Necessary for the robot-gripper controll.
### ```robotiq_preamble.py```
Necessary for the UR5e gripper.



