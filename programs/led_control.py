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
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    pixels.fill((r,g,b))

def off():
    global wheel_execute
    global rainbow_execute
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


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow():
    global rainbow_execute
    if not rainbow_execute:
        rainbow_execute = True
        x = threading.Thread(target=rainbow_cycle, args=())
        x.start()

def rainbow_cycle(wait):
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)

    global rainbow_execute
    while (rainbow_execute):
     for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait


while True:
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

    rainbow_cycle(0)  # Increa