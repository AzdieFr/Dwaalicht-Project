# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel
from varspeed import Vspeed
import timer
from timer import Timer

timer = Timer()
timer2 = Timer()

pixel_pin = board.D13
num_pixels = 58

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


#VSpeed setup
vs_output = Vspeed(init_position=0, result="int")
vs_output.set_bounds(lower_bound=-1, upper_bound=255)
vs_output2 = Vspeed(init_position=0, result="int")
vs_output2.set_bounds(lower_bound=0, upper_bound=255)

#sequence for making lights fade
color_chase_sequence = [
   (0, 0, 1, "LinearInOut"),
   (num_pixels*2, 1, num_pixels*2, "LinearInOut"),
]

gradient_sequence = [
    (0, 0.01, 1, "LinearInOut"),
    (255, 1, 10, "QuadEaseInOut"),
    (0, 1, 10, "QuadEaseInOut"),
]



RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)


timer_on  = False
timer2_on  = False

while True:

    if not timer_on:
        timer.start()
        timer.set_duration(10)
        timer_on = True

    if timer.expired():
        if not timer2_on:
            timer2.start()
            timer2.set_duration(3)
            timer2_on = True
        position_output, running_output, changed_output = vs_output.sequence(sequence=color_chase_sequence, loop_max=0)
        if (position_output < num_pixels):
            for i in range(position_output):
                pixels[i] = GREEN
        else:
            for i in range(position_output%num_pixels):
                pixels[i] = CYAN
        pixels.show()

        if timer2.expired():
            print("timer2 expired")
            timer_on = False
            timer2_on = False
    else:
        position_output1, running_output1, changed_output1 = vs_output2.sequence(sequence=gradient_sequence, loop_max=0)
        pixels.fill((0, 255, position_output1))
        pixels.show()




