
from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from robotiq_gripper_control import RobotiqGripper
import copy
from CalculatePositions import ChessPositionsCalculator
import testChess as tc
import Getuci



class URClass:
    getuci = Getuci.Getuci()
    def __init__(self):
        self.rtde_c = RTDEControl("172.31.1.144")
        self.rtde_r = RTDEReceive("172.31.1.144")
        self.gripper = RobotiqGripper(self.rtde_c)
        self.gripper.set_force(50)  # from 0 to 100 %
        self.gripper.set_speed(100)  # from 0 to 100 %
        self.speed = 0.5
        self.acceleration = 0.3
        self.gripper.move(100)
        self.standardPosition = [-0.01748171324078468, 0.4066080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        self.chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
    
    def moveSimple(self, pos):
        idlePos = self.rtde_c.moveL(pos)
        print('Hello move simple')


#___________________________________________________________________________________________
    def get_uci_to_split(self, uci): # Takes the uci string and declares it in two functions.
        #Additionaly i need the color, so i know which player i must find the UCI for. 
        self.uci = uci

        self.a(self.uci) #Startsquare the robot will move piece from! 
        #How to make the urclass eat each of these, a and b- function's? 
        self.b(self.uci)#Endsquare the robot will move piece to!

    def a(self, startUCI): #Splits the uci to get start square
        self.startuci=startUCI
        fra = self.startuci[:2]
        return fra
    
    def b(self,sluttUCI):#Splits the uci to get end square
        self.sluttuci = sluttUCI
        til= self.sluttuci[2:]
        return til
#___________________________________________________________________________________________



    def walking():
        print('Walking...')


    def carefull(self):
        self.gripper.move(100)
        sjakkbrikke = ChessPositionsCalculator.getPosition('a1')
        sjakkbrikke[2] = ChessPositionsCalculator.elevate()
        løftArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        


    def moverob(self, a, b):
        idlePos = self.rtde_c.moveL(ChessPositionsCalculator.startPosition())
        sjakkbrikke = ChessPositionsCalculator.getPosition(a)
        GårTilPosisjon = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        sjakkbrikke[2] = ChessPositionsCalculator.lower()
        senkArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        self.gripper.move(10)

        sjakkbrikke[2] = ChessPositionsCalculator.elevate()
        løftArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        sjakkbrikke = ChessPositionsCalculator.getPosition(b)
        GårTilPosisjon = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        løftArmIgjen = copy.deepcopy(sjakkbrikke) #Deepcopy
        sjakkbrikke[2] = ChessPositionsCalculator.lower()
        senkArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        self.gripper.move(50)
        
        GårTilPosisjon = self.rtde_c.moveL(løftArmIgjen,0.25,1.2,False)
        idlePos = self.rtde_c.moveL(ChessPositionsCalculator.startPosition())

    def startPosition(self):
        self.standardPosition = [-0.01748171324078468, 0.4066080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        
    
    

    
    def lower(self):
        self.chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        self.gripperheight = self.chess_orgin[2]
        self.gripperheight-=0.10
        
    
    def elevate():
        0.19681733919878186

    
    
    def getPosition(brikkePos):
        chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        length = 0.058
        chessboard_dict ={}
        list_pos = ['a','b','c','d','e','f','g','h']
        #Creating a 8x8 chess map
        for i in range(8):
            for j in range(8):
                postion = f"{list_pos[j]}{i+1}"
                x = chess_orgin[0]+j*length
                y = chess_orgin[1]+i*length
                z = chess_orgin[2]
                Rx= chess_orgin[3]
                Ry= chess_orgin[4]
                Rz= chess_orgin[5]
                chessboard_dict[postion] = [x,y,z,Rx,Ry,Rz]
        pos_a1 = chessboard_dict.get(brikkePos)
        print(pos_a1)
        return pos_a1
    
    if __name__ == '__main__':
        pass






