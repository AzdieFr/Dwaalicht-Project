import board
import time
from varspeed import Vspeed
import digitalio
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from analogio import AnalogOut
import pwmio
import p9813
from vibration_motor import VibrationMotor

#Vibration motor setup
vibration_motor = VibrationMotor()

#Led setup
pin_clk = board.D13
pin_data = board.D10
num_leds = 1
led = p9813.P9813(pin_clk, pin_data, num_leds)

#Potentiometer setup
potmeter = AnalogIn(board.A2)
#button setup
button = DigitalInOut(board.D4)
button.direction = Direction.INPUT

#VSpeed setup
#Opinionator
vs_outputopinion1 = Vspeed(init_position=0, result="int")
vs_outputopinion1.set_bounds(lower_bound=0, upper_bound=255)
vs_outputopinion2 = Vspeed(init_position=0, result="int")
vs_outputopinion2.set_bounds(lower_bound=0, upper_bound=255)
vs_outputopinion3 = Vspeed(init_position=0, result="int")
vs_outputopinion3.set_bounds(lower_bound=0, upper_bound=255)
vs_outputopinion4 = Vspeed(init_position=0, result="int")
vs_outputopinion4.set_bounds(lower_bound=0, upper_bound=255)

#emotional damage
vs_outputemo1 = Vspeed(init_position=0, result="int")
vs_outputemo1.set_bounds(lower_bound=0, upper_bound=255)
vs_outputemo2 = Vspeed(init_position=0, result="int")
vs_outputemo2.set_bounds(lower_bound=0, upper_bound=255)
vs_outputemo3 = Vspeed(init_position=0, result="int")
vs_outputemo3.set_bounds(lower_bound=0, upper_bound=255)
vs_outputemo4 = Vspeed(init_position=0, result="int")
vs_outputemo4.set_bounds(lower_bound=0, upper_bound=255)
vs_outputemo5 = Vspeed(init_position=0, result="int")
vs_outputemo5.set_bounds(lower_bound=0, upper_bound=255)

#forest
vs_outputforest1 = Vspeed(init_position=0, result="int")
vs_outputforest1.set_bounds(lower_bound=0, upper_bound=255)
vs_outputforest2 = Vspeed(init_position=0, result="int")
vs_outputforest2.set_bounds(lower_bound=0, upper_bound=255)

#animal abuse
vs_outputanimal = Vspeed(init_position=0, result="int")
vs_outputanimal.set_bounds(lower_bound=0, upper_bound=255)
vs_outputanimal1 = Vspeed(init_position=0, result="int")
vs_outputanimal1.set_bounds(lower_bound=0, upper_bound=255)
vs_outputanimal2 = Vspeed(init_position=0, result="int")
vs_outputanimal2.set_bounds(lower_bound=0, upper_bound=255)
vs_outputanimal3 = Vspeed(init_position=0, result="int")
vs_outputanimal3.set_bounds(lower_bound=0, upper_bound=255)

#billip pheesley
vs_outputphillip1 = Vspeed(init_position=0, result="int")
vs_outputphillip1 .set_bounds(lower_bound=0, upper_bound=255)
vs_outputphillip2  = Vspeed(init_position=0, result="int")
vs_outputphillip2 .set_bounds(lower_bound=0, upper_bound=255)

#overig
vs_outputoverig1 = Vspeed(init_position=0, result="int")
vs_outputoverig1.set_bounds(lower_bound=0, upper_bound=255)
vs_outputoverig2 = Vspeed(init_position=0, result="int")
vs_outputoverig2.set_bounds(lower_bound=0, upper_bound=255)

#different sequences
#opnionator
gradient_sequence1 = [
    (255, 0.01, 1, "LinearInOut"),
    (150, 0.5, 10, "LinearInOut"),
    (255, 0.5, 10, "LinearInOut"),
]

gradient_sequence2 = [
    (128, 0.01, 1, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (128, 0.5, 10, "LinearInOut"),
]

gradient_sequence3 = [
    (0, 0.01, 1, "LinearInOut"),
    (255, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
]

vibration_sequence1 = [
    (0, 0.01, 1, "LinearInOut"),
    (0, 0.40, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (1, 0.2, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (0, 0.40, 1, "LinearInOut"),
]

#emotional damage
fading_sequence1 = [
    (0, 0.01, 1, "LinearInOut"),
    (154, 1, 10, "LinearInOut"),
    (0, 1, 10, "LinearInOut"),
]
fading_sequence2 = [
    (0, 0.01, 1, "LinearInOut"),
    (255, 1, 10, "LinearInOut"),
    (0, 1, 10, "LinearInOut"),
]
fading_sequence3 = [
    (0, 0.01, 1, "LinearInOut"),
    (255, 1, 10, "LinearInOut"),
    (0, 1, 10, "LinearInOut"),
]

anxious_sequence = [
    (0, 0.01, 1, "LinearInOut"),
    (255, 0.05, 1, "LinearInOut"),
    (0, 0.05, 1, "LinearInOut"),
]

vibration_sequence2 = [
    (0, 0.01, 1, "LinearInOut"),
    (1, 0.8, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (0, 0.8, 1, "LinearInOut"),
]

#Forest
forest_sequence1 = [
    (0, 0.01, 1, "LinearInOut"),
    (255, 0.01, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (255, 0.01, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (255, 0.01, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (0, 0.5, 1, "LinearInOut"),
]
forest_sequence2 = [
    (0, 0.01, 1, "LinearInOut"),
    (75, 0.01, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (75, 0.01, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (75, 0.01, 1, "LinearInOut"),
    (0, 0.01, 1, "LinearInOut"),
    (0, 0.5, 1, "LinearInOut"),
]

#animal abuse
animal_sequence1 = [
    (0, 0.01, 1, "LinearInOut"),
    (13, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (255, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
]
animal_sequence2 = [
    (0, 0.01, 1, "LinearInOut"),
    (152, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (255, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (255, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
]
animal_sequence3 = [
    (0, 0.01, 1, "LinearInOut"),
    (186, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
]
animalvibration_sequence = [
    (0, 0.01, 1, "LinearInOut"),
    (0, 0.75, 1, "LinearInOut"),
    (1, 0.1, 1, "LinearInOut"),
    (0, 0.1, 1, "LinearInOut"),
    (0, 0.76, 1, "LinearInOut"),
]

#billip pheesley
chain_sequence = [
    (0, 0.01, 1, "LinearInOut"),
    (100, 1.5, 10, "LinearInOut"),
    (0, 1, 10, "LinearInOut"),
    (100, 1, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (100, 0.5, 10, "LinearInOut"),
    (0, 0.25, 10, "LinearInOut"),
    (100, 0.25, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 2, 1, "LinearInOut"),
    (100, 1.5, 10, "LinearInOut"),
    (0, 1, 10, "LinearInOut"),
    (100, 1, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (100, 0.5, 10, "LinearInOut"),
    (0, 0.25, 10, "LinearInOut"),
    (100, 0.25, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 2.5, 1, "LinearInOut"),
    (100, 1.5, 20, "LinearInOut"),
    (0, 1.25, 15, "LinearInOut"),
    (100, 1.25, 15, "LinearInOut"),
    (0, 1, 10, "LinearInOut"),
    (100, 1, 10, "LinearInOut"),
    (0, 0.75, 10, "LinearInOut"),
    (100, 0.75, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (100, 0.5, 10, "LinearInOut"),
    (0, 0.25, 10, "LinearInOut"),
    (100, 0.25, 10, "LinearInOut"),
    (0, 0.5, 10, "LinearInOut"),
    (0, 1, 1, "LinearInOut"),
]

moth_sequence = [
    (0, 0.01, 1, "LinearInOut"),
    (0, 1, 1, "LinearInOut"),
    (1, 0.5, 1, "LinearInOut"),
    (0, 2, 1, "LinearInOut"),
    (1, 2, 1, "LinearInOut"),
    (0, 0.5, 1, "LinearInOut"),
    (1, 1.5, 1, "LinearInOut"),
    (0, 3, 1, "LinearInOut"),
    (1, 2, 1, "LinearInOut"),
    (0, 1, 1, "LinearInOut"),
    (1, 2, 1, "LinearInOut"),
    (0, 2.5, 1, "LinearInOut"),
]

#overig
overig_sequence = [
    (0, 0.01, 1, "LinearInOut"),
    (255, 1, 10, "LinearInOut"),
    (0, 1, 10, "LinearInOut"),
]

#mapping function
def map(v, input_min, input_max, output_min, output_max):
    return (v - input_min) / (input_max - input_min) * (output_max - output_min) + output_min


#orange purple gradient
orange = (255,128,0)
purple = (150,0,255)
cyan = (154, 255, 255)
animalblue = (13,152,186)
yellow = (255, 255, 0)

#=========================================================================================================================
#*************************************************************************************************************************
#=========================================================================================================================


while True:
#     print(potmeter.value)
    pot = potmeter.value
    distance = map(pot,128,65520,0,1)
#     print(distance)
    if distance > 0 and distance < 0.2:
        print("opinionator")
        position_output, running_output, changed_output = vs_outputopinion1.sequence(sequence=vibration_sequence1, loop_max=0)
        position_output1, running_output1, changed_output1 = vs_outputopinion2.sequence(sequence=gradient_sequence1, loop_max=0)
        position_output2, running_output2, changed_output2 = vs_outputopinion3.sequence(sequence=gradient_sequence2, loop_max=0)
        position_output3, running_output3, changed_output3 = vs_outputopinion4.sequence(sequence=gradient_sequence3, loop_max=0)

        vibration_motor.update(position_output)
        led.fill((position_output1, position_output2, position_output3))
        led.write()
    elif distance > 0.2 and distance < 0.4:
        print("emotional damage")
        if button.value:
            #anxious
            position_output4, running_output4, changed_output4 = vs_outputemo1.sequence(sequence=anxious_sequence, loop_max=0)
            led.fill((position_output4, 0,0))
            led.write()
            vibration_motor.update(position_output4)
        else:
            #calm
            position_output5, running_output5, changed_output5 = vs_outputemo2.sequence(sequence=vibration_sequence2, loop_max=0)
            position_output6, running_output6, changed_output6 = vs_outputemo3.sequence(sequence=fading_sequence1, loop_max=0)
            position_output7, running_output7, changed_output7 = vs_outputemo4.sequence(sequence=fading_sequence2, loop_max=0)
            position_output8, running_output8, changed_output8 = vs_outputemo5.sequence(sequence=fading_sequence3, loop_max=0)

            vibration_motor.update(position_output5)
            led.fill((position_output6, position_output7, position_output8))
            led.write()

    elif distance > 0.4 and distance < 0.6:
        print("forest")
        position_output9, running_output9, changed_output9 = vs_outputforest1.sequence(sequence=forest_sequence1, loop_max=0)
        position_output10, running_output10, changed_output10 = vs_outputforest2.sequence(sequence=forest_sequence2, loop_max=0)

        vibration_motor.update(position_output9)
        led.fill((position_output10, position_output9, position_output10))
        led.write()

    elif distance > 0.6 and distance < 0.8:
        print("animal abuse")
        position_output13, running_output13, changed_output13 = vs_outputanimal.sequence(sequence=animal_sequence1, loop_max=0)
        position_output14, running_output14, changed_output14 = vs_outputanimal1.sequence(sequence=animal_sequence2, loop_max=0)
        position_output15, running_output15, changed_output15 = vs_outputanimal2.sequence(sequence=animal_sequence3, loop_max=0)
        position_output16, running_output16, changed_output16 = vs_outputanimal3.sequence(sequence=animalvibration_sequence, loop_max=0)

        vibration_motor.update(position_output16)
        led.fill((position_output13, position_output14, position_output15))
        led.write()

    elif distance > 0.8 and distance < 1:
        print("billip pheesley")
        position_output17, running_output17, changed_output17 = vs_outputphillip1.sequence(sequence=chain_sequence, loop_max=0)
        position_output18, running_output18, changed_output18 = vs_outputphillip2.sequence(sequence=moth_sequence, loop_max=0)

        vibration_motor.update(position_output18)
        led.fill((0, int(186*(position_output17/100)), int(255*(position_output17/100))))
        led.write()

    else:
        print("overig")
        position_output11, running_output11, changed_output11 = vs_outputoverig1.sequence(sequence=overig_sequence, loop_max=0)
        position_output12, running_output12, changed_output12 = vs_outputoverig2.sequence(sequence=vibration_sequence2, loop_max=0)

        vibration_motor.update(position_output12)
        led.fill((0, 0, position_output11))
        led.write()
    time.sleep(0.1)


