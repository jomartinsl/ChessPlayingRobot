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


    def get_safe_move(self, input1, input2): #Wait's 3 seconds before getting the UCI
        self.input1 = input1
        self.input2 = input2
        loop = asyncio.get_event_loop()
        dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"])
        # b_old = loop.run_until_complete(dgt.get_board()) 
        self.input1 = loop.run_until_complete(dgt.get_board()) 

        while True:
            last_change_time = time.time()
            while True:
                self.input2 = loop.run_until_complete(dgt.get_board()) 
                last_input2 = self.input2

                if self.input1 != last_input2:
                    last_change_time = time.time()
                    self.input1 = last_input2
                
                #Wait's three seconds before confirming the move.
                elif self.input1==last_input2 and time.time() - last_change_time >= 3: 
                    #Checks if the piece has been in the same place for 3 seconds or more
                    boardStatusLast = loop.run_until_complete(dgt.get_board()) 
                    return boardStatusLast
            
                
    def only_the_move_value(self):
        pass

        




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
                
            elif self.sammenlign_og_lagre_svar(B_old,b_old)==False: #This compares the two boards, old and new, and if there is a difference, the whileloop will loop once!.
                # When the board is changed, for instance: a piece has been picked up, it loop's once.
                teller=1
                
            time.sleep(0.01)
        b_old=B_old
        uci = self.getuci.get_uci(b_old, self.get_safe_move(b_old,b_new))#uses class Getuci.py to calculate the uci. 
        #Also it takes in the  function get_safe_move ^. This makes it posible to slide the pieces. 
        if uci!="":
            # print(uci) #Print's out the uci, 'b2b4'
            return uci
        b_old=b_new



    def the_robot_moves(self):
        loop = asyncio.get_event_loop()
        dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"]) #Gets the board status. 
        firstMove = loop.run_until_complete(dgt.get_board()) 
        middleMove=loop.run_until_complete(dgt.get_board())
        teller = 0
        Done = False
        while not Done:
            lastMove = loop.run_until_complete(dgt.get_board()) 
            if self.sammenlign_og_lagre_svar(firstMove,lastMove) == True:
                firstMove= lastMove
                teller+=1
                if teller>=2:
                    Done=True
                
    def fen(self):
        loop = asyncio.get_event_loop()
        dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"]) #Gets the board status. 
        return loop.run_until_complete(dgt.get_board()) 


    

    def sanMove(self): 
        # returns the final SAN
        return self.human_san(self.reads_human_uci())


#NB!: Need's to check up against legal moves before executing
    def human_san(self,uci_move): #Takes in the UCI and transform it to SAN value
        self.testUCI = uci_move
        fra = self.testUCI[:2] # Splits the uci-value into two, so we can put it in the move variable. The chess.Move() takes in two inputs, from-square and to-square.
        til = self.testUCI[2:]
        move=chess.Move(fra,til)
        move=move.from_uci(self.testUCI)
        san = self.virtualBoard.san(move) # This is the san value which we use to feed the chess engine.
        print(f'testChess virtualboard:\n{self.virtualBoard}')
        return san
    


    def a(self, startUCI): #Splits the uci to get start square
        self.startuci=startUCI
        fra = self.startuci[:2]
        return fra
    
    def b(self,sluttUCI):#Splits the uci to get end square
        self.sluttuci = sluttUCI
        til= self.sluttuci[2:]
        return til

    if __name__=='__main__':
        pass



