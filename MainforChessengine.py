import ChessEngine as ce
import chess as ch
import testChess as te
import Getuci 
import URClass as ur

urclass = ur.URClass()
getuci = Getuci.Getuci()
testChess = te.testChess()

class MainforChessengine:

    def __init__(self, board=testChess.virtualBoard):
        self.board=board

    #play human move
    def playHumanMove(self):
        san = testChess.sanMove()
        legal_moves = self.board.legal_moves
        self.play = san
        
            
        
        try:
            #Get human move
            # print(self.board)
            #Push human move
            self.board.push_san(self.play)
            return
        except:
            self.playHumanMove()
        

    #play engine move
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove()) 
        
    def getEngineMove(self, maxDepth, color): #This return's a UCI!
        engine = ce.Engine(self.board, maxDepth, color)
        bestMove=engine.getBestMove()
        print('Engine UCI-move: ',bestMove)
        return bestMove

        

    #start a game
    def startGame(self):
        #get human player's color
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Choose depth: """))
        if color=="b":
            while (self.board.is_checkmate()==False):
                print("The engine is thinking...")
                uciForRobot = self.getEngineMove(maxDepth, ch.WHITE) 
                a=testChess.a(str(uciForRobot)) #Split's uci into two pieces and grabs the start square
                b=testChess.b(str(uciForRobot))
                urclass.moverob(a,b,'b')
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            #print(self.board.outcome())    

        elif color=="w": #If the human player is 'white', the robot will play as black, and this is the black playerside.
            while (self.board.is_checkmate()==False):
                #print(self.board)
                self.playHumanMove()
                print(f'MainforChessengine w1:\n{self.board}')
                uciForRobot = self.getEngineMove(maxDepth, ch.BLACK) #This is the UCI that has to be split up and fed to the robotarm!!
                # print(uciForRobot)
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.BLACK)
                a=testChess.a(str(uciForRobot)) #Split's uci into two pieces and grabs the start square
                b=testChess.b(str(uciForRobot))
                # print(f'a: {a} og b: {b}')
                print(f'MainforChessengine w2:\n{self.board}')
                urclass.moverob(a,b,'w') # Takes in from- and to-square and the robotarm preforms the movement
                testChess.the_robot_moves() #Let's the robot move a piece for black
                
                

            print(self.board.outcome())
        #reset the board
        self.board.reset
        #start another game
        start_new_game = input('Nytt parti, "j" for ja og "n" for nei')
        if start_new_game == 'j':
            self.startGame()
        elif start_new_game == 'n':
            print('Takk for kampen.')


# if __name__== '__main__':
    # newBoard = ch.Board()
    # game = MainforChessengine(newBoard)
    # bruh = game.startGame()
#create an instance and start a game