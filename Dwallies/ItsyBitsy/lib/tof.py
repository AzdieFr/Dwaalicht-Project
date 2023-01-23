# Tof.py

import time
import board
import busio
import adafruit_vl53l0x

class Tof():
    def __init__(self, pin0, pin1):
        self.i2c = busio.I2C(pin0, pin1)
        self.vl53 = adafruit_vl53l0x.VL53L0X(self.i2c)

    def sense(self, distance):
        return self.vl53.range < distance

    def sense_range(self):
        return self.vl53.range
