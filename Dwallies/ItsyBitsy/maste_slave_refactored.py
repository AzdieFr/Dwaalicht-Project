# This is a test version of the organized final code
# Do not copy this code - some elements may differ between Dwallies!

import board
import time
import busio
import pwmio
import neopixel
import random

import sound_library as slib
import sequences as s
import timers_library as tlib
import vspeed_setup_library as vslib
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket

from digitalio import DigitalInOut, Direction
from vibration_motor import VibrationMotor
from adafruit_esp32spi import adafruit_esp32spi
from i2cperipheral import I2CPeripheral
from DFPlayer import DFPlayer

#DF player setup
PLAYER_VOL = 100
dfplayer = DFPlayer(volume=PLAYER_VOL)              # creates uart internally
playing = False
time.sleep(0.200)

#Vibration motor setup
vibration_motor = VibrationMotor()

#Led setup
pixel_pin = board.D13
num_pixels = 1
led = neopixel.NeoPixel(pixel_pin, num_pixels, brightness = 0.3, auto_write=False)

#button setup
button = DigitalInOut(board.D4)
button.direction = Direction.INPUT

#timers_setup
tlib.setup_timers()

#VSpeed setup
vslib.vspeed_setup()

regs = [0] * 16
index = 0
previous_state = 0
tlib.timer_randomness.start()
i = random.randint(0, 10)
testing = False

with I2CPeripheral(board.SCL, board.SDA, (0x40, 0x41)) as device:

    while True:

        if(tlib.timer_randomness.expired()):
            tlib.timer_randomness.start()
            i = random.randint(0, 10)

        r = device.request()
        if not r or testing:
            state = previous_state
            print("No connection. State is equal: " + str(state))
            #continue

        if(r):
            with r:  # Closes the transfer if necessary by sending a NACK or feeding dummy bytes
                if r.address == 0x40:
                    if not r.is_read:  # Main write which is Selected read
                        b = r.read(1)
                        if not b or b[0] > 15:
                            break
                        index = b[0]
                        b = r.read(1)
                        if b:
                            regs[index] = b[0]
                    elif r.is_restart:  # Combined transfer: This is the Main read message
                        n = r.write(bytes([regs[index]]))
                   #  else:
    #                     A read transfer is not supported in this example
    #                     If the microcontroller tries, it will get 0xff byte(s) by the ctx manager (r.close())
                elif r.address == 0x41:
                    print("I'm in 41")
                    if not r.is_read:
                        state = int.from_bytes(r.read(), "big")
                        if(state == 0):
                            state = previous_state
                        print("I received connection. The state is: " + str(state))
                        b = r.read(1)
                        if b and b[0] == 0xde:
                            led.fill((255,0,0))
                            led.show()
                            pass
        #here do stuff after the check
        previous_state = state

        if(tlib.playing_timer.expired()):
            playing = False

        if(state == 0):
            print("State is 0")

        if(state == 1):
            print("opinionator")
            position_output, running_output, changed_output = vslib.vs_outputopinion1.sequence(sequence = s.vibration_sequence1, loop_max=0)
            position_output1, running_output1, changed_output1 = vslib.vs_outputopinion2.sequence(sequence = s.gradient_sequence1, loop_max=0)
            position_output2, running_output2, changed_output2 = vslib.vs_outputopinion3.sequence(sequence = s.gradient_sequence2, loop_max=0)
            position_output3, running_output3, changed_output3 = vslib.vs_outputopinion4.sequence(sequence = s.gradient_sequence3, loop_max=0)
            vibration_motor.update(position_output)
            led.fill((position_output2, position_output1, position_output3))
            led.show()
            if(not tlib.opinion_timer_on):
                tlib.opinion_timer.start()
                tlib.opinion_timer_on = True
            if(tlib.opinion_timer.expired() and (playing == False)):
                playing = True
                dfplayer.play(track=slib.CRAZY_SOUND)
                tlib.playing_timer.start()
                tlib.opinion_timer_on = False

        elif(state == 2):
            print("emotional damage")
            if (i % 2 == 0):
                #anxious
                position_output4, running_output4, changed_output4 = vslib.vs_outputemo1.sequence(sequence = s.anxious_sequence, loop_max=0)
                led.fill((0, position_output4, 0))
                led.show()
                vibration_motor.update(position_output4)
            else:
                #calm
                position_output5, running_output5, changed_output5 = vslib.vs_outputemo2.sequence(sequence = s.vibration_sequence2, loop_max=0)
                position_output7, running_output7, changed_output7 = vslib.vs_outputemo4.sequence(sequence = s.fading_sequence2, loop_max=0)
                vibration_motor.update(position_output5)
                led.fill((int(255 * (position_output7/255)), int(40 * (position_output7/255)) , int(255 * (position_output7/255))))
                led.show()
            if(not tlib.emotional_damage_timer_on):
                tlib.emotional_damage_timer.start()
                tlib.emotional_damage_timer_on = True
            if(tlib.emotional_damage_timer.expired() and (playing == False)):
                playing = True
                dfplayer.play(track = slib.EMOTIONAL_DAMAGE_SOUND)
                tlib.playing_timer.start()
                tlib.emotional_damage_timer_on = False

        elif(state == 3):
            print("forest")
            position_output9, running_output9, changed_output9 = vslib.vs_outputforest1.sequence(sequence = s.forest_sequence1, loop_max=0)
            vibration_motor.update(position_output9)
            led.fill((int(255 * (position_output9/255)), int(75 * (position_output9/255)), int(255 * (position_output9/255))))
            led.show()
            if(not tlib.forest_timer_on):
                tlib.forest_timer.start()
                tlib.forest_timer_on = True
            if(tlib.forest_timer.expired() and (playing == False)):
                playing = True
                dfplayer.play(track = slib.FOREST_SOUND)
                tlib.playing_timer.start()
                tlib.forest_timer_on = False

        elif(state == 4):
            print("animal abuse")
            position_output13, running_output13, changed_output13 = vslib.vs_outputanimal.sequence(sequence = s.animal_sequence1, loop_max=0)
            position_output14, running_output14, changed_output14 = vslib.vs_outputanimal1.sequence(sequence = s.animal_sequence2, loop_max=0)
            position_output15, running_output15, changed_output15 = vslib.vs_outputanimal2.sequence(sequence = s.animal_sequence3, loop_max=0)
            position_output16, running_output16, changed_output16 = vslib.vs_outputanimal3.sequence(sequence = s.animalvibration_sequence, loop_max=0)
            vibration_motor.update(position_output16)
            led.fill((position_output13, position_output14, position_output15))
            led.show()
            if(not tlib.animal_timer_on):
                tlib.animal_timer.start()
                tlib.animal_timer_on = True
            if(tlib.animal_timer.expired() and (playing == False)):
                playing = True
                dfplayer.play(track = slib.ANIMAL_ABUSE_SOUND)
                tlib.playing_timer.start()
                tlib.animal_timer_on = False

        elif (state == 5):
            print("billip pheesley")
            position_output17, running_output17, changed_output17 = vslib.vs_outputphillip1.sequence(sequence = s.chain_sequence, loop_max=0)
            position_output18, running_output18, changed_output18 = vslib.vs_outputphillip2.sequence(sequence = s.moth_sequence, loop_max=0)
            vibration_motor.update(position_output18)
            led.fill((int(186*(position_output17/100)), 0, int(255*(position_output17/100))))
            led.show()
            if(not tlib.philip_timer_on):
                tlib.philip_timer.start()
                tlib.philip_timer_on = True
            if(tlib.philip_timer.expired() and (playing == False)):
                playing = True
                dfplayer.play(track = slib.HAPPY_SOUND)
                tlib.playing_timer.start()
                tlib.philip_timer_on = False

        else:
            print("overig")
            position_output11, running_output11, changed_output11 = vslib.vs_outputoverig1.sequence(sequence = s.overig_sequence, loop_max=0)
            position_output12, running_output12, changed_output12 = vslib.vs_outputoverig2.sequence(sequence = s.vibration_sequence2, loop_max=0)
            vibration_motor.update(position_output12)
            led.fill((0, 0, position_output11))
            led.show()
            previous_state = 0
            if(not tlib.overig_timer_on):
                tlib.overig_timer.start()
                tlib.overig_timer_on = True
            if(tlib.overig_timer.expired() and (playing == False)):
                playing = True
                dfplayer.play(track = slib.SAD_SOUND)
                tlib.playing_timer.start()
                tlib.overig_timer_on = False
        time.sleep(0.1)
