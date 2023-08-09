import testChess as tc
import Getuci as gu
import MainforChessengine
import chess as ch


# import URClass as ur              #Comment out if you want to run the chess program
# urclass = ur.URClass()            #Else if you want to test or run simple programs from URClass, uncomment
mainEngine= MainforChessengine.MainforChessengine()
testChess = tc.testChess()
getUciandSan = tc.testChess()




board = ch.Board()
game = MainforChessengine.MainforChessengine(testChess.virtualBoard)
startGame = game.startGame()
print('NB: Main file 1')



# urclass.moverob('a1','b1')
# urclass.moveSimple()


# urclass.a1_field_hover()


