import smbus
import time
 
bus = smbus.SMBus(1)
 
# L3GD20 address, 0x69
bus.write_byte_data(0x69, 0x20, 0x0F)
bus.write_byte_data(0x69, 0x23, 0x30)
time.sleep(0.5)
 
# Read X-Axis data
data0 = bus.read_byte_data(0x69, 0x28)
data1 = bus.read_byte_data(0x69, 0x29)
 
xGyro = data1 * 256 + data0
if xGyro > 32767 :
	xGyro -= 65536
 
# Read Y-Axis data
data0 = bus.read_byte_data(0x69, 0x2A)
data1 = bus.read_byte_data(0x69, 0x2B)
 
yGyro = data1 * 256 + data0
if yGyro > 32767 :
	yGyro -= 65536
 
# Read Z-Axis data
data0 = bus.read_byte_data(0x69, 0x2C)
data1 = bus.read_byte_data(0x69, 0x2D)
 
# Convert the data
zGyro = data1 * 256 + data0
if zGyro > 32767 :
	zGyro -= 65536
 
# Output data to screen
print "Rotation in X-Axis : %d" %xGyro
print "Rotation in Y-Axis : %d" %yGyro
print "Rotation in Z-Axis : %d" %zGyro
