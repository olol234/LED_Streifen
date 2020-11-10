import board
import neopixel
import threading
import time
import random

num_pixels = 109
pixels = neopixel.NeoPixel(board.D18, num_pixels)
wheel_execute = False
wheel_execute2 = False

def green():
    pixels.fill((9,138,236))

def random():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pixels.fill((r,g,b))

def off():
    global wheel_execute
    wheel_execute = False
    pixels.fill((0,0,0))

def colorpicker(color_string):

    color_string = color_string.lstrip('#')
    hlen = len(color_string)
    pixels.fill(tuple(int(color_string[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)))

def wheel_thread():
    colors = [(255,0,0),
              (255,90,0),
              (255,255,0),
              (51,255,0),
              (0,255,204),
              (0,200,255),
              (0,0,255),
              (200,0,255),
              ]
    i = 0
    global wheel_execute
    while (wheel_execute):
        time.sleep(2)
        pixels.fill(colors[i])
        i += 1
        if (i >= len(colors)):
            i = 0
def wheel():
    global wheel_execute
    if not wheel_execute:
        wheel_execute = True
        x = threading.Thread(target=wheel_thread, args=())
        x.start()

def wheel2():
    global wheel_execute2
    if not wheel_execute2:
        wheel_execute2 = True
        x = threading.Thread(target=wheel2_thread, args=())
        x.start()

def wheel2_thread():
    pos = 90
    global wheel_execute2
    while (wheel_execute2):
        time.sleep(2)
        if pos < 85:
        pixels.fill((pos * 3, 255 - pos * 3, 0))
        elif pos < 170:
        pos -= 85
        pixels.fill((255 - pos * 3, 0, pos * 3))
        else:
        pos -= 170
        pixels.fill((0, pos * 3, 255 - pos * 3))