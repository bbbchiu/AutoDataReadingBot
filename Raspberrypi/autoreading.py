import sys
from gy801 import GY801
from gps import GPS

a = GY801()
b = GPS()

print("Reading ACC data (m/s/s)")
a.accReading()

print("Reading GYRO data (degree per second )")
a.gyReading()

print("Reading MAG data")
#a.magReading()

print("Reading Temperature and Pressure")
a. airReading()

print("Reading GPS data")
b.gpsReading()

