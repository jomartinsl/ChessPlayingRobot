import asyncio
import asyncdgt
import ChessEngine as ce
import chess
import time
import copy
import Getuci as gu


class testChess:


    def __init__(self, board=chess.Board()):
        self.virtualBoard=board

    def sammenlign_og_lagre_svar(self, gammelt_svar, nytt_svar):
        if gammelt_svar != nytt_svar:
            return True
        else:
            return False


    getuci=gu.Getuci()



    def reads_human_uci(self):
        moveList = list(self.virtualBoard.legal_moves)
        
        loop = asyncio.get_event_loop()
        dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"])
        # color = input('"w" or "b": ')
        teller = 1
        b_old = loop.run_until_complete(dgt.get_board())
        B_old = loop.run_until_complete(dgt.get_board())
        
        while teller%3 !=0:
            b_new = loop.run_until_complete(dgt.get_board())
            if self.sammenlign_og_lagre_svar(b_old,b_new) ==True:
                b_old=b_new
                teller+=1
                
            elif self.sammenlign_og_lagre_svar(B_old,b_old)==False:
                teller=1
                
            time.sleep(0.01)
        b_old=B_old
        uci = self.getuci.get_uci(b_old, b_new)
        if uci!="":
            print(uci)
            return uci
    
        # elif self.sammenlign_og_lagre_svar(b_old,b_new)==-1:
            # print('Make a move')
        # time.sleep(1)
        b_old=b_new


    def check_var_in_list(self, list, uci):
        found_match = False

        for var in list:
            if var == uci:
                print(f"Match found: {uci}")
                found_match = True
                return uci
        
        if not found_match:
            print("Illegal move")

    def boardStatus(self):
        # print(self.virtualBoard)
        # print('Legal moves: ', self.virtualBoard.legal_moves)
        return self.virtualBoard
    

    def sanMove(self):
        return self.human_san(self.reads_human_uci())


    def human_san(self,uci_move):
        self.testUCI = uci_move
        fra = self.testUCI[:2]
        til = self.testUCI[2:]
        move=chess.Move(fra,til)
        move=move.from_uci(self.testUCI)
        san = self.virtualBoard.san(move)
        return san

    if __name__=='__main__':
        pass



