import time
import board
import adafruit_mpu6050
from components.buzzer import Buzzer


i2c = board.I2C()  # uses board.SCL and board.SDA
mpu = adafruit_mpu6050.MPU6050(i2c)
mylist = [-9.8,-9.8,-9.8,-9.8,-9.8]

buzzer = Buzzer()

while True:
    isPeak = False
    x, y, z = mpu.acceleration
    print((x,y,z))
    print("")

    average = (mylist[0] + mylist[1] + mylist[2] + mylist[3] + mylist[4])/5

    print("average: ", + average)
    print(mylist)
    if mylist[0] > (average + 0.7) or mylist[0] < (average - 0.7):
        print("peak")
        buzzer.update(50)
        isPeak = True
        mylist.pop(0)
        mylist.insert(0,z)

    if isPeak == False:
        buzzer.update(0)
        mylist.insert(0,z)
        mylist.pop(5)
    time.sleep(0.1)
