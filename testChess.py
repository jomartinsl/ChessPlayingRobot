import asyncio
import asyncdgt
import ChessEngine as ce
import chess
import time
import copy




loop = asyncio.get_event_loop()
dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"])




nums = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h"}
def get_uci(board1, board2, who_moved):
    str_board = str(board1).split("\n")
    str_board2 = str(board2).split("\n")
    move = ""
    flip = False
    if who_moved == "w":
        for i in range(8)[::-1]:
            for x in range(15)[::-1]:   
                if str_board[i][x] != str_board2[i][x]:
                    if str_board[i][x] == "." and move == "":
                        flip = True
                    move+=str(nums.get(round(x/2)+1))+str(9-(i+1))
    else:
        for i in range(8):
            for x in range(15):
                if str_board[i][x] != str_board2[i][x]:
                    if str_board[i][x] == "." and move == "":
                        flip = True
                    move+=str(nums.get(round(x/2)+1))+str(9-(i+1))
    if flip:
        move = move[2]+move[3]+move[0]+move[1]
    return move


def sammenlign_og_lagre_svar(gammelt_svar, nytt_svar):
    if gammelt_svar != nytt_svar:
        return True
    else:
        return False


color = input('"w" or "b": ')

def uci():
    teller = 1
    b_old = loop.run_until_complete(dgt.get_board())
    B_old = loop.run_until_complete(dgt.get_board())
    while True:
        while teller%3 !=0:
            b_new = loop.run_until_complete(dgt.get_board())
            if sammenlign_og_lagre_svar(b_old,b_new) ==True:
                b_old=b_new
                teller+=1
            time.sleep(0.01)
        b_old=B_old
        uci = get_uci(b_old, b_new, color)
        if uci!="":
            print(uci)
            return uci  
        elif sammenlign_og_lagre_svar(b_old,b_new)==-1:
            print('Make a move')
        time.sleep(1)
        b_old=b_new



def human_san(uci_move):
    testUCI = uci_move
    fra = testUCI[:2]
    til = testUCI[2:]
    move=chess.Move(fra,til)
    viritualBoard=chess.Board()
    move=move.from_uci(testUCI)
    san = viritualBoard.san(move)
    viritualBoard.push_san(san)
    BSAN=print(san) #Denne skal bli sendt til chess engine
    return san


if __name__=='__main__':
    human_san(uci())



########################################################

# print(loop.run_until_complete(dgt.get_board()))
# print(type(loop.run_until_complete(dgt.get_board()))) 
# board = loop.run_until_complete(dgt.get_board().board_fen())
# board_.set_fen(board.board_fen())
# last_move = board_.peek()
# lsdt_movr_uci = last_move.uci()
# fen_=board.board_fen()
