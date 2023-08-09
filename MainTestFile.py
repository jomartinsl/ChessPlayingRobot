import testChess as tc
import Getuci as gu
import MainforChessengine as ClassChessEngine
import chess as ch
# import URClass as ur

# urclass = ur.URClass()
mainEngine= ClassChessEngine.MainforChessengine()
testChess = tc.testChess()
getUciandSan = tc.testChess()




board = ch.Board()
game = ClassChessEngine.MainforChessengine(testChess.virtualBoard)
startGame = game.startGame()
print('NB: Main file 1')
# urclass.moverob('a1','b1')


# getUciandSan.human_san(testChess.reads_human_uci())
# testChess.boardStatus()
# getUciandSan.human_san(testChess.reads_human_uci())
