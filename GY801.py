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

    def accReading(self):
        pass
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