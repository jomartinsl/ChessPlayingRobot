import ChessEngine as ce
import chess as ch
import testChess as te


testChess = te.testChess()

class MainforChessengine:

    def __init__(self, board=testChess.virtualBoard):
        self.board=board

    #play human move
    def playHumanMove(self):
        teller = 0
        san = testChess.sanMove()
        self.play = san
        try:
            #get human move
            teller +=1
            print(self.board)
            #Push human move
            self.board.push_san(self.play)
            return
        except:
            self.playHumanMove()
        

    #play engine move
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())
        print('play engine move ble tatt i bruk')
        
    def getEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        bestMove=engine.getBestMove()
        print('ChessEngine: ',bestMove)

        

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
                self.playEngineMove(maxDepth, ch.WHITE)
                print("board1",self.board)
                self.playHumanMove()
                print("board2",self.board)
            print(self.board)
            print(self.board.outcome())    

        elif color=="w":
            while (self.board.is_checkmate()==False):
                print("board3",self.board)
                self.playHumanMove()
                # self.board.push_san(self.play)
                print("board4",self.board)
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
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