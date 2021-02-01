import smbus

class H3C5883L:
    def __init__(self):
        self.init_reg()
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(self.address,self.rega,0x70)
        self.bus.write_byte_data(self.address,self.regb,0xa0)
        self.bus.write_byte_data(self.address,self.regmode,0x00)

    def init_reg(self):
        self.address = 0x30
        self.rega = 0x00
        self.regb = 0x01
        self.regmode = 0x02
        self.ctrl_reg4 = 0x23
        self.ctrl_reg5 = 0x24
        self.reference = 0x25
        self.x_l = 0x04
        self.x_h = 0x03
        self.y_l = 0x06
        self.y_h = 0x05
        self.z_l = 0x08
        self.z_h = 0x07
        

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

    def getMag(self):
        return self.x,self.y,self.z
