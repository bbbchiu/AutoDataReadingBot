import smbus
import time
from adxl345 import ADXL345
from l3g4200d import L3G4200D
from h3c5883l import H3C5883L 

class GY801:
    def __init__(self):
        self.accx = 0
        self.accy = 0
        self.accz = 0
        self.gx = 0
        self.gy = 0
        self.gz = 0
        self.magx = 0
        self.magy = 0
        self.magz = 0
        self.airPressure = 0
        self.numRecord = 10
        self.timeInteration = 1

    def accReading(self):        
        device_acc = ADXL345()
        i = self.numRecord
        while(i > 0):
            device_acc.read_data()
            self.accx, self.accy, self.accz = device_acc.getAcc()
            print("x = %.4f (m/s)" % ( self.accx ))
            print("y = %.4f (m/s)" % ( self.accy ))
            print("z = %.4f (m/s)" % ( self.accz ))
            print("\n")
            time.sleep(self.timeInteration)
            i-=1

    def gyReading(self):
        device_gy = L3G4200D()
        i = self.numRecord
        while(i > 0):
            device_gy.read_data()
            self.gx,self.gy,self.gz = device_gy.getGyro()
            print("Rotation in X-Axis : %d" %self.gx)
            print("Rotation in Y-Axis : %d" %self.gy)
            print("Rotation in Z-Axis : %d" %self.gz)         
            print("\n")
            time.sleep(self.timeInteration)
            i-=1

    def magReading(self):
        device_mag = H3C5883L()
        i = self.numRecord
        while(i > 0):
            device_mag.read_data()
            self.magx,self.magy,self.magz = device_mag.getMag()
            print("Mag in X-Axis : %4f" %self.magx)
            print("Mag in Y-Axis : %4f" %self.magy)
            print("Mag in Z-Axis : %4f" %self.magz)
            print("\n")
            time.sleep(self.timeInteration)
            i-=1

    def airReading(self):
        pass

    def gy2degree(self):
        self.degreex = 0
        self.degreey = 0
        self.degreez = 0

    def air2height(self):
        self.height = 0
