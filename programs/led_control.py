import board
import neopixel
import threading
import time
import random

num_pixels = 109
pixels = neopixel.NeoPixel(board.D18, num_pixels)
wheel_execute = False

def green():
    pixels.fill((9,138,236))

def random():
    pixels.fill((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))

def off():
    global wheel_execute
    wheel_execute = False
    pixels.fill((0,0,0))

def colorpicker(color_string):

    color_string = color_string.lstrip('#')
    hlen = len(color_string)
    pixels.fill(tuple(int(color_string[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)))

def wheel_thread():
    pos = 0
    global wheel_execute
    while (wheel_execute):
        time.sleep(2)
        if pos < 85:
            pixels.fill((pos, 255 - pos, 0))
            pos = 255 - pos
        elif pos < 170:
            pixels.fill((255 - pos , 0, pos ))
            pos -= 90
        else:
            pixels.fill((0, pos, 255 - pos ))
            pos -= 90

def wheel():
    global wheel_execute
    if not wheel_execute:
        wheel_execute = True
        x = threading.Thread(target=wheel_thread, args=())
        x.start()