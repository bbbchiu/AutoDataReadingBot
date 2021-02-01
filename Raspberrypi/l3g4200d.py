import smbus

class L3G4200D:
    def __init__(self):
        self.init_reg()
        self.bus = smbus.SMBus(1)
        self.bus.write_byte_data(self.address,self.ctrl_reg1,0x0F)
        self.bus.write_byte_data(self.address,self.ctrl_reg4,0x30)

    def init_reg(self):
        self.address = 0x69
        self.ctrl_reg1 = 0x20
        self.ctrl_reg2 = 0x21
        self.ctrl_reg3 = 0x22
        self.ctrl_reg4 = 0x23
        self.ctrl_reg5 = 0x24
        self.reference = 0x25
        self.x_l = 0x28
        self.x_h = 0x29
        self.y_l = 0x2A
        self.y_h = 0x2B
        self.z_l = 0x2C
        self.z_h = 0x2D
        

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

    def getGyro(self):
        return self.x,self.y,self.z
