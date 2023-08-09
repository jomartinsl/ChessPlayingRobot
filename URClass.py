
from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from robotiq_gripper_control import RobotiqGripper
import copy
# from CalculatePositions import ChessPositionsCalculator
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
        self.speed = 0.1
        self.acceleration = 0.1
        self.gripper.move(50)
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



    def carefull(self):
        self.gripper.move(100)
        sjakkbrikke = self.getPosition('a1')
        sjakkbrikke[2] = self.elevate()
        løftArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        


    def moverob(self, a, b, color):
        self.color = color
        self.gripper.move(50)
        self.startSquare = a
        self.endSquare = b
        idlePos = self.rtde_c.moveL(self.startPosition(),0.25,1.2,False)
        if self.color=='w':
            sjakkbrikke = self.getPositionForBlack(self.startSquare)
        elif self.color == 'b':
            sjakkbrikke = self.getPositionForWhite(self.startSquare)
        GårTilPosisjon = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        sjakkbrikke[2] = self.lower()
        senkArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        self.gripper.move(10)
        sjakkbrikke[2]=self.elevate()
        løftArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        if self.color == 'w':
            sjakkbrikke = self.getPositionForBlack(self.endSquare)
        elif self.color == 'b':
            sjakkbrikke = self.getPositionForWhite(self.endSquare)
        GårTilPosisjon = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        løftArmIgjen = copy.deepcopy(sjakkbrikke) #Deepcopy
        sjakkbrikke[2] = self.lower()
        senkArm = self.rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        self.gripper.move(50)
        
        GårTilPosisjon = self.rtde_c.moveL(løftArmIgjen,0.25,1.2,False)
        idlePos = self.rtde_c.moveL(self.startPosition())

   
    def startPosition(self):
        standardPosition = [-0.01748171324078468, 0.4066080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        return standardPosition

    

    def lower(self): #Universal, you can adjust the height without disturping the other index
        chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        gripperheight = chess_orgin[2]
        gripperheight-=0.10
        return gripperheight
        
    
    def elevate(self):
        self.chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        # self.chess_orgin[2]+=0.11 #Lifts the arm up 11 cm
        return 0.19681733919878186

    def a1_field_hover(self):
        self.chess_orgin = [-0.257817132407847, 0.4816080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        hover = self.rtde_c.moveL(self.chess_orgin,0.25,1.2,False)
        # self.chess_orgin[0] -= 0.045 # høyre og venstre
        # self.chess_orgin[1] -= 0.020 # frem og tilbake
        self.chess_orgin[2] -= 0.090 #opp og ned
        # return self.chess_orgin
        senkArm = self.rtde_c.moveL(self.chess_orgin,0.25,1.2,False)


    
    def getPositionForWhite(self, brikkePos):
        self.chess_orgin = [-0.257817132407847, 0.4816080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        self.length = 0.055
        self.chessboard_dict ={}
        list_pos = ['a','b','c','d','e','f','g','h']
        #Creating a 8x8 chess map
        for i in range(8):
            for j in range(8):
                postion = f"{list_pos[j]}{i+1}"
                x = self.chess_orgin[0]+j*self.length
                y = self.chess_orgin[1]+i*self.length
                z = self.chess_orgin[2]
                Rx= self.chess_orgin[3]
                Ry= self.chess_orgin[4]
                Rz= self.chess_orgin[5]
                self.chessboard_dict[postion] = [x,y,z,Rx,Ry,Rz]
        pos_a1 = self.chessboard_dict.get(brikkePos)
        # print('this is pos_a1: ',pos_a1) #Print's the [n-1...n+1] for the positions for the different squares 
        return pos_a1
    
    def getPositionForBlack(self, brikkePos):
        self.chess_orgin = [-0.257817132407847, 0.4816080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        self.length = 0.055
        self.chessboard_dict ={}
        list_pos = ['a','b','c','d','e','f','g','h']
        #Creating a 8x8 chess map
        for i in range(8):
            for j in range(8):
                postion = f"{list_pos[7-i]}{8-j}"
                x = self.chess_orgin[0]+i*self.length
                y = self.chess_orgin[1]+j*self.length
                z = self.chess_orgin[2]
                Rx= self.chess_orgin[3]
                Ry= self.chess_orgin[4]
                Rz= self.chess_orgin[5]
                self.chessboard_dict[postion] = [x,y,z,Rx,Ry,Rz]
        pos_a1 = self.chessboard_dict.get(brikkePos)
        # print('this is pos_a1: ',pos_a1) #Print's the [n-1...n+1] for the positions for the different squares 
        return pos_a1
    
    if __name__ == '__main__':
        pass