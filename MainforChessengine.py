import ChessEngine as ce
import chess as ch
import testChess as te
import Getuci 
import URClass as ur
import threading

urclass = ur.URClass()
getuci = Getuci.Getuci()
testChess = te.testChess()

class MainforChessengine:

    def __init__(self, board=testChess.virtualBoard):
        self.board=board

    #play human move
    def playHumanMove(self):
        san = testChess.sanMove()
        self.play = san    
        print('Human san: ',san)

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
        return engine
        # self.board.push(engine.getBestMove()) #Ta denne tilbake om krasj, 
        
    def getEngineMove(self, maxDepth, color): #This return's a UCI!
        engine = ce.Engine(self.board, maxDepth, color)
        bestMove=engine.getBestMove()
        # print('Engine UCI-move: ',bestMove)
        return bestMove

        

    #start a game
    def startGame(self):
        urclass.startPositionStartChess()
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
                print(uciForRobot)
                self.scanBoard1 = testChess.fen()
                a=testChess.a(str(uciForRobot)) #Split's uci into two pieces and grabs the start square
                b=testChess.b(str(uciForRobot))
                urclass.moverob(a,b,'b')
                self.scanBoard2 = testChess.fen()
                uci = getuci.get_uci(self.scanBoard1,self.scanBoard2)
                san = testChess.human_uci_to_san(uci)
                self.board.push_san(san)
                print(f'board rett etter roboten har bevegd seg:\n {self.board}')
                # print(self.playEngineMove(maxDepth, ch.WHITE)) #This playes the move from the robot engine.
                self.playHumanMove()
            print(self.board.outcome())    

        elif color=="w": #If the human player is 'white', the robot will play as black, and this is the black playerside.
            while (self.board.is_checkmate()==False):
                self.playHumanMove()
                uciForRobot = self.getEngineMove(maxDepth, ch.BLACK) #This is the UCI that has to be split up and fed to the robotarm!!
                a=testChess.a(str(uciForRobot)) #Split's uci into two pieces and grabs the start square
                b=testChess.b(str(uciForRobot))
                scanBoard1 = testChess.fen()
                legal_moves = self.board.legal_moves
                print(legal_moves)
                urclass.moverob(a,b,'w') # Takes in from- and to-square and the robotarm preforms the movement
                scanBoard2 = testChess.fen()
                uci = getuci.get_uci(scanBoard1,scanBoard2)
                #Need to find a way to push moves like 'Qxd5' which means 'Queen captures d5' and 'Kxf3+' which means Knight captures f3 and checks the king. 
                print(uci)
                san = testChess.human_uci_to_san(uci)
                # done = False
                # for move in legal_moves:
                #     while not done:
                #         if san == move:
                #             self.board.push_san(san)
                #             done = True
                #         if len(legal_moves) == legal_moves.count:
                #             self.board.pop()
                self.board.push_san(san)
                print('san verdi til robot: ',san)
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