import smbus
import time
from adxl345 import ADXL345

class gy801:
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
        self.accReading()
	
    def accReading(self):        
        adxl345 = ADXL345()
        while(True):
            axes = adxl345.getAxes(True)
            print "ADXL345 on address 0x%x:" % (adxl345.address)
            print "   x = %.3fG" % ( axes['x'] )
            print "   y = %.3fG" % ( axes['y'] )
            print "   z = %.3fG" % ( axes['z'] )
            time.sleep(1)

    def gyReading(self):
        self.gy2degree()
    def magReading(self):
        pass
    def airReading(self):
        pass

    def gy2degree(self):
        self.degreex = 0
        self.degreey = 0
        self.degreez = 0

    def air2height(self):
        self.height = 0
