# led.py

import board
import p9813

class LED():
    def __init__(self, num_leds):
        self.pin_clk = board.D13
        self.pin_data = board.D10
        self.num_leds = num_leds
        self.leds = p9813.P9813(self.pin_clk, self.pin_data, self.num_leds)

    # Update the LED with specified intensity for all three color channels
    def update(self, color):
        color = max(0, min(color, 255))
        self.leds.fill((color, color, color))
        self.leds.write()

    # Update the LED with a tuple of (RED, GREEN, BLUE)
    def update_full_color(self, color):
        clipped_color = (max(0, min(color[0], 255)),
            max(0, min(color[1], 255)),
            max(0, min(color[2], 255)))
        self.leds.fill(clipped_color)
        self.leds.write()
