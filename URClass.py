
from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from robotiq_gripper_control import RobotiqGripper
import copy
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
        self.speed = 0.16
        self.acceleration = 0.1
        self.gripper.move(30)       #Tilbake og frem     Venstre og høyre       Ned og opp          Rx                  Ry                      Rz
        self.standardPosition = [-0.01748171324078468, 0.4066080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        self.chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]


    
    def moveSimple(self, pos):
        idlePos = self.rtde_c.moveL(pos)
        print('Hello move simple')


    def a(self, startUCI): #Splits the uci to get start square
        self.startuci=startUCI
        fra = self.startuci[:2]
        return fra
    
    def b(self,sluttUCI):#Splits the uci to get end square
        self.sluttuci = sluttUCI
        til= self.sluttuci[2:]
        return til



        


    def moverob(self, a, b, color):
        self.color = color
        self.gripper.move(30)
        self.startSquare = a
        self.endSquare = b
        idlePos = self.rtde_c.moveL(self.startPosition(),self.speed,1.2,False)
        if self.color=='w':
            sjakkbrikke = self.getPositionForBlack(self.startSquare)
        elif self.color == 'b':
            sjakkbrikke = self.getPositionForWhite(self.startSquare)
        GårTilPosisjon = self.rtde_c.moveL(sjakkbrikke,self.speed,1.2,False)
        sjakkbrikke[2] = self.lower()
        senkArm = self.rtde_c.moveL(sjakkbrikke,self.speed,1.2,False)
        self.gripper.move(8)
        sjakkbrikke[2]=self.elevate()
        løftArm = self.rtde_c.moveL(sjakkbrikke,self.speed,1.2,False)
        if self.color == 'w':
            sjakkbrikke = self.getPositionForBlack(self.endSquare)
        elif self.color == 'b':
            sjakkbrikke = self.getPositionForWhite(self.endSquare)
        GårTilPosisjon = self.rtde_c.moveL(sjakkbrikke,self.speed,1.2,False)
        sjakkbrikke[2] = self.lower()+0.0015
        senkArm = self.rtde_c.moveL(sjakkbrikke,self.speed,1.2,False)
        self.gripper.move(30)
        sjakkbrikke[2] = self.elevate()
        GårTilPosisjon = self.rtde_c.moveL(sjakkbrikke,self.speed,1.2,False)
        idlePos = self.rtde_c.moveL(self.startPosition(),self.speed,1.2,False)

   
    def startPosition(self):
        standardPosition = [0.3801738000939013, -0.01797368394369248, 0.19634970458215878, -2.188840390553494, 2.2278318427863804, 0.02402116883245557]
        return standardPosition

    #Position's the robot in startposition whenever a new game start's
    def startPositionStartChess(self):
        self.standardPosition = [0.3801738000939013, -0.01797368394369248, 0.19634970458215878, -2.188840390553494, 2.2278318427863804, 0.02402116883245557]
        idlePos = self.rtde_c.moveL(self.standardPosition,self.speed,1.2,False) 
    

    def lower(self): #Universal, you can adjust the height without disturping the other index
        #Ned for å plukke opp piece 
        lower = 0.13041471525894038 - 0.123 #Trekker fra slik at armen ikke treffer brettet eller pieces, 0.27 er standardhøyden, og -0.13 er hvor mye den går ned
        # print('lower 1: ', lower)
        return lower #Returns the subtrakted height. 
        
    
    def elevate(self):
        #Løfter armen med 10 cm #Lift's the robotarm 10 cm up
        #Løfte piece opp
        elevate = -0.0004147152589403791+0.123
        return elevate


    #This gets the positions if the robotarm plays as 'white'
    def getPositionForWhite(self, brikkePos):
        self.chess_orgin = [0.3875662750671822, 0.17044196628472913, 0.13041471525894038, -2.1487047112310784, 2.255092571981374, 0.02006373937944305]
        self.length = 0.05525
        self.chessboard_dict ={}
        list_pos = ['a','b','c','d','e','f','g','h']
        #Creating a 8x8 chess map
        for i in range(8):
            for j in range(8):
                postion = f"{list_pos[i]}{j+1}"
                x = self.chess_orgin[0]+i*self.length
                y = self.chess_orgin[1]+j*self.length
                z = self.chess_orgin[2]
                Rx= self.chess_orgin[3]
                Ry= self.chess_orgin[4]
                Rz= self.chess_orgin[5]
                self.chessboard_dict[postion] = [x,y,z,Rx,Ry,Rz]
        pos_a1 = self.chessboard_dict.get(brikkePos)
        return pos_a1
    
    #This gets the positions if the robotarm plays as 'black'
    def getPositionForBlack(self, brikkePos):
        self.chess_orgin = [0.3875662750671822, 0.17044196628472913, 0.13041471525894038, -2.1487047112310784, 2.255092571981374, 0.02006373937944305]
        
        self.length = 0.055
        self.chessboard_dict ={}
        list_pos = ['a','b','c','d','e','f','g','h']
        #Creating a 8x8 chess map
        for i in range(8):
            for j in range(8):
                postion = f"{list_pos[7-i]}{8-j}"
                x = self.chess_orgin[0]+j*self.length
                y = self.chess_orgin[1]-i*self.length
                z = self.chess_orgin[2]
                Rx= self.chess_orgin[3]
                Ry= self.chess_orgin[4]
                Rz= self.chess_orgin[5]
                self.chessboard_dict[postion] = [x,y,z,Rx,Ry,Rz]
        pos_a1 = self.chessboard_dict.get(brikkePos)
        return pos_a1

    def testingRobmovement(self):
        startpos = [0.3875662750671822, 0.17044196628472913, 0.13041471525894038, -2.1487047112310784, 2.255092571981374, 0.02006373937944305]
        self.rtde_c.moveL(startpos,self.speed,1.2,False)
        startpos[0]+=0.1
        self.rtde_c.moveL(startpos,self.speed,1.2,False)
        startpos[0]-=0.1
        self.rtde_c.moveL(startpos,self.speed,1.2,False)
        input('hvilken retning???')
        startpos[1]+=0.1
        self.rtde_c.moveL(startpos,self.speed,1.2,False)
        startpos[1]-=0.1
        self.rtde_c.moveL(startpos,self.speed,1.2,False)
        input('hvilken retning???')
    if __name__ == '__main__':
        pass