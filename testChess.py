import asyncio
import asyncdgt
import ChessEngine as ce
import chess
import time
import copy
import Getuci as gu


class testChess:


    def __init__(self, board=chess.Board()):
        self.virtualBoard=board #Creates a viritual board which follows every moves and gets updatet whenever a move is beeing taken. 
                                #This makes it posible to get a overview over the legal moves and these sorts of thing on the way. 

    def sammenlign_og_lagre_svar(self, gammelt_svar, nytt_svar): #Compares two inputs. This is to make the counter go up, since we want it to break the while loop after 2 itterations.

        if gammelt_svar != nytt_svar:
            return True
        else:
            return False


    getuci=gu.Getuci()



    def reads_human_uci(self): #Returns UCI. 
        
        loop = asyncio.get_event_loop()
        dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"]) #Gets the board status. 
        # color = input('"w" or "b": ')
        teller = 1
        # Get board twice
        b_old = loop.run_until_complete(dgt.get_board()) 
        B_old = loop.run_until_complete(dgt.get_board())
        
        while teller%3 !=0: #Ends when player gives two different board states.
            b_new = loop.run_until_complete(dgt.get_board())
            if self.sammenlign_og_lagre_svar(b_old,b_new) ==True:
                b_old=b_new
                teller+=1
                
            elif self.sammenlign_og_lagre_svar(B_old,b_old)==False: #The point of this was: if someone place the piece they 
                #picked up back to the same position. Because this will act as if it was a sincire move. But right now it doesnt work.
                teller=1
                
            time.sleep(0.01)
        b_old=B_old
        uci = self.getuci.get_uci(b_old, b_new)#uses class Getuci.py to calculate the uci
        if uci!="":
            print(uci)
            return uci
        b_old=b_new


    

    def boardStatus(self):
        # print(self.virtualBoard)
        # print('Legal moves: ', self.virtualBoard.legal_moves)
        return self.virtualBoard
    

    def sanMove(self): 
        # returns the final SAN
        return self.human_san(self.reads_human_uci())


    def human_san(self,uci_move):
        self.testUCI = uci_move
        fra = self.testUCI[:2] # Splits the uci-value into two, so we can put it in the move variable. The chess.Move() takes in two inputs, from-square and to-square.
        til = self.testUCI[2:]
        move=chess.Move(fra,til)
        move=move.from_uci(self.testUCI)
        san = self.virtualBoard.san(move) # This is the san value which we use to feed the chess engine.
        return san

    if __name__=='__main__':
        pass



