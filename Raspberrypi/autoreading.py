import sys
from gy801 import GY801

a = GY801()

ans = input('which device do you what to read? (acc,gyro,mag,bmp)')

if ans == 'acc':
    print("start getting acc data")
    a.accReading()
elif ans == 'gyro':
    print("start getting gyro data")
    a.gyReading()
elif ans == 'mag':
    a.magReading()
elif ans == 'bmp':
    pass
else:
    pass
