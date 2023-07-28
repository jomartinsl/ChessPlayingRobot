# Chess playing robot

This project's is about getting a UR5e robotarm to play chess against you. We have a DGT-board and a UR5e robot to disposition.
The code for this project is divided in two. We have the chess-python code and ur5e-code. 
#
### What the project is currently doing:
* It can get the state of the DGT board and translate it into SAN and UCI values, which is very usefull from futher code. 
* The robotarm knows every chess-square, and can move to all of them and pick and place the pieces. The only input needed is the UCI, which has to be devided into two string/variables.
* Choose degree of difficulty and color ('white' or 'black').
* Can get a SAN move, put it in the engine, and get a counterplay in the terminal window. 
#
### What the project needs:
* It needs a new way to interpret moves. Now it scans the board twice and whatever square the piece lands on will be the move nomatter what. So for instance if I pick up the Night and put it back, the program thinks it's the move and get's traceback. The way the code runs now, is if it's only legal moves without human errors. 
* Get a way to accept captures, and this is the same issue as the one over. This goes on in the same class, `testChess.py`. 
* Spesial moves: *En passant* and *castling* is not taken into account. 

#

Still working on the gripper and some code in connection with the moving pieces buisness. 


The ```MainTestFile.py``` is where the program runs from. This is where you call the ```URClass.py``` and ```MainforChessengine.py``` and get the program to run.

Under the different classes is beeing described:

* #### ```MainTestFile```
  Start's the game.


* #### ```URClass.py```
  This class, ```URClass.py``` is used for the UR5-e robot arm. You controll the starting position, which is where it's ready to make the next move, and the code 
  for all the 64-squares at the chessboard. 
  The robot is controlled with TCP, tool-centre-point, to every position. The 'moverob()' function is where you want to put the start-square and the end-square 
  when the robot is making a move. Example Nc3 -> from-square = b1, to-square = c3. B1 and c3 will be put in as parametre in the function. 'moverob('b1', 'c3'). 
  The designations are something that repeats itself, for example 'Nc3' is a "san" value and 'b1c3' is a "uci" value which is important to understand the code.

* #### ```MainforChessengine.py```
  This is where the chessengine talks with the DGT board. The move that is been played will be sent to this class and the engine will make the best or worst move 
  in return. The startGame() function is located in this class. This is where the move you made will be pushed on the viritual chessboard.

* #### ```ChessEngine.py```
  This the part you dont touch. This is the chessengine that calculate the best move, depends on the depth/difficulity you are playing on. High depth makes the 
  engine better, but also takes longer time to answer with a good move.

* #### ```testChess.py```
  This class is mainly used for converting the move that has been made, into san-value. For instance if you move the pawn from e2 to e4 it will return the san- 
  value 'e4'. When the dgt-board detects a change in the pattern it will scan the current state and save the previous state. The only task for this class is to 
  return one value which is the **san-value**. There is also declared a viritual chessboard in this class. This chessboard are going to copy every move that is 
  beeing made so it can have track of check's, en passant's, checkmate's and these sorts of things. This comes with the 'import chess' library. 

* #### ```Getuci.py```
  Converts the board status to 'uci'. It need to compare two status in order for it to return a UCI. This is set to always white in the class, because it's work 
  under progress. The function in this class is named get_uci() and takes two parametre, but in the starting point it took three, and the third was the color ("b" 
  or "w"). I found it a little difficult to pass the color variable into this, but for a better programmer I dont think it will be an issue.

* #### ```robotiq_gripper_control.py```
  Necessary for the robot-gripper controll.

* #### ```robotiq_preamble.py```
  Necessary for the UR5e gripper.



