import smbus

class ADXL345:
    def __init__(self):
        self.init_reg()
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(self.address,self.power_ctl,0x08)
        self.bus.write_byte_data(self.address,self.bw_rate,0x0B)

    def init_reg(self):
        self.address = 0x53
        self.power_ctl = 0x2D
        self.bw_rate = 0x2C
        self.x_l = 0x32
        self.x_h = 0x33
        self.y_l = 0x34
        self.y_h = 0x35
        self.z_l = 0x36
        self.z_h = 0x37
        

    def read_data(self):
        self.x = self.bus.read_byte_data(self.address,self.x_h)*256+self.bus.read_byte_data(self.address,self.x_l)
        if self.x > 32767:
            self.x -= 65536

        self.y = self.bus.read_byte_data(self.address,self.y_h)*256+self.bus.read_byte_data(self.address,self.y_l)
        if self.y > 32767:
            self.y -= 65536

        self.z = self.bus.read_byte_data(self.address,self.z_h)*256+self.bus.read_byte_data(self.address,self.z_l)
        if self.z > 32767:
            self.z -= 65536

        self.data2acc()

    def data2acc(self):
        self.x *= 0.004*9.8
        self.y *= 0.004*9.8
        self.z *= 0.004*9.8

    def getAcc(self):
        return self.x,self.y,self.z
