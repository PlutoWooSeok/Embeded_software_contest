import serial

import time



class Robot():



    def __init__(self, serial = None):

        self.serial = serial



    def TX_data(self, one_byte):

        self.serial.write(serial.to_bytes([one_byte]))

        

    '''********************************************'''

    def go_left(self, time = 0.1):

        self.TX_data(1)

        time.sleep(time)

    

    def go_right(self):

        self.TX_data(2)

        time.sleep(0.1)

    

    def left_walk(self):

        self.TX_data(3)

        time.sleep(0.1)

    

    def right_walk(self):

        self.TX_data(4)

        time.sleep(0.1)

        

    def walk12(self):

        for i in range(6):

            self.TX_data(1)

            time.sleep(2.5)

            self.TX_data(2)

            time.sleep(2.5)

    

    def left_turn(self):

        self.TX_data(5)

        time.sleep(0.1)



    def right_turn(self):

        self.TX_data(6)

        time.sleep(0.1)

        

    def left_turn90(self):

        for i in range(0,3):

            self.TX_data(7)

            time.sleep(1)

        self.TX_data(5)

        time.sleep(1)

        self.TX_data(4)

        time.sleep(1)

        #self.TX_data(1)

        #time.sleep(2)

    

    def right_turn90(self):

        for i in range(0,4):

            self.TX_data(8)

            time.sleep(1)

        self.TX_data(6)

        time.sleep(1)

        #self.TX_data(1)

        #time.sleep(2)

        

    def left_turn180(self):

        for i in range(0,6):

            self.TX_data(7)

            time.sleep(1)

        self.TX_data(5)

        time.sleep(0.1)

    

    def right_turn180(self):

        for i in range(0,8):

            self.TX_data(8)

            time.sleep(1)

        self.TX_data(6)

        time.sleep(0.1)

        

    def stand(self):

        self.TX_data(9)

        time.sleep(0.1)

        

    def swalk(self):

        self.TX_data(10)

        time.sleep(0.1)

        

    def head_100(self):

        self.TX_data(11)

        time.sleep(0.1)

        

    def head_110(self):

        self.TX_data(12)

        time.sleep(0.1)

    

    def head_120(self):

        self.TX_data(13)

        time.sleep(0.1)

        

    def head_130(self):

        self.TX_data(14)

        time.sleep(0.1)

        

    def head_140(self):

        self.TX_data(15)

        time.sleep(0.1)

        

    def head_150(self):

        self.TX_data(17)

        time.sleep(0.1)

    

    def head_160(self):

        self.TX_data(18)

        time.sleep(0.1)

        

    def head_170(self):

        self.TX_data(19)

        time.sleep(0.1)

        

    def head_180(self):

        self.TX_data(20)

        time.sleep(0.1)

        

    '''******************mission*******************'''

    

    def up_stair(self):

        for i in range(3):

            self.TX_data(21)

            time.sleep(7)

            self.TX_data(6)

            time.sleep(1)

            self.TX_data(5)

            time.sleep(1)

        

    def down_stair(self):

        for i in range(3):

            self.TX_data(22)

            time.sleep(9)

        

    def hit_bell(self):

        self.TX_data(23)

        time.sleep(0.1)

    

    def pick_up(self):

        self.TX_data(24)

        time.sleep(0.1)

        

    def pick_up_left_walk(self):

        self.TX_data(25)

        time.sleep(0.1)

    

    def pick_up_right_walk(self):

        self.TX_data(26)

        time.sleep(0.1)

        

    def pick_up_left_turn(self):

        self.TX_data(27)

        time.sleep(0.1)

    

    def pick_up_right_turn(self):

        self.TX_data(28)

        time.sleep(0.1)    

    

    def throw_away(self):

        self.TX_data(29)

        time.sleep(0.1)

    

    '''*******************sound********************'''



    def east(self):

        self.TX_data(41)

        time.sleep(0.1)

        

    def west(self):

        self.TX_data(42)

        time.sleep(0.1)

        

    def south(self):

        self.TX_data(43)

        time.sleep(0.1)

        

    def north(self):

        self.TX_data(44)

        time.sleep(0.1)

        

    def safe_area(self):

        self.TX_data(45)

        time.sleep(0.1)

    

    def covid_area(self):

        self.TX_data(46)

        time.sleep(0.1)

        

    def danger_area(self):

        self.TX_data(47)

        time.sleep(0.1)

        

    def help(self):

        self.TX_data(48)

        time.sleep(0.1)

        

    def A_area(self):

        self.TX_data(49)

        time.sleep(0.1)

        

    def B_area(self):

        self.TX_data(50)

        time.sleep(0.1)

        

    def C_area(self):

        self.TX_data(51)

        time.sleep(0.1)

    

    def D_area(self):

        self.TX_data(52)

        time.sleep(0.1)

    



