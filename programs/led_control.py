import board
import neopixel
import threading
import time
import random

num_pixels = 100
pixels = neopixel.NeoPixel(board.D18, num_pixels,auto_write = False)

wheel_execute = False
fadergb_execute = False
theaterchase_execute = False

def green():
    pixels.fill((9,138,236))
    pixels.show()


def test():
    pixels.fill((100,138,236))
    pixels.show()

def off():
    pixels.fill((0,0,0))
    pixels.show()

def reset():
    global wheel_execute
    global fadergb_execute
    global theaterchase_execute
    wheel_execute = False
    fadergb_execute = False
    theaterchase_execute = False
    pixels.fill((0,0,0))
    pixels.show()

def colorpicker(color_string):

    color_string = color_string.lstrip('#')
    hlen = len(color_string)
    pixels.fill(tuple(int(color_string[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)))
    pixels.show()

def wheel_thread(wait=1):
    pos = 0
    global wheel_execute
    while (wheel_execute):
        if pos < 85:
            pixels.fill((pos, 255 - pos, 0))
            pos = 255 - pos
        elif pos < 170:
            pixels.fill((255 - pos , 0, pos ))
            pos -= 90
        else:
            pixels.fill((0, pos, 255 - pos ))
            pos -= 90
    pixels.show()
    time.sleep(wait)

def wheel():
    global wheel_execute
    if not wheel_execute:
        wheel_execute = True
        x = threading.Thread(target=wheel_thread, args=())
        x.start()



def fadergb_thread():
    global fadergb_execute
    while (fadergb_execute):
        for i in range(0, 3):
            for j in range(0, 255):
                if i == 0:
                    pixels.fill((j, 0, 0))
                elif i == 1:
                    pixels.fill((0, j, 0))
                elif i == 2:
                    pixels.fill((0, 0, j))
                pixels.show()

            for j in range(255, 0, -1):
                if i == 0:
                    pixels.fill((j, 0, 0))
                elif i == 1:
                    pixels.fill((0, j, 0))
                elif i == 2:
                    pixels.fill((0, 0, j))
                pixels.show()

def fadergb():
    global fadergb_execute
    if not fadergb_execute:
        fadergb_execute = True
        x = threading.Thread(target=fadergb_thread, args=())
        x.start()

def theaterchase():
    global theaterchase_execute
    if not theaterchase_execute:
        theaterchase_execute = True
        x = threading.Thread(target=theaterchase_thread, args=())
        x.start()

def theaterchase_thread(wait=0.3):
    global theaterchase_execute
    while (theaterchase_execute):
        for j in range(0,255,30):
            for k in range(0,3):
                for i in range(num_pixels-k):
                    if i %3 == 0:
                        pixels[i+k] = rainbowcolor((j+i)%255)
                    else:
                        pixels[i+k] = (0,0,0)
                time.sleep(wait)
                pixels.show()

def rainbowcolor(wheel_pos):
    if wheel_pos < 85:
        return (wheel_pos * 3, 255 - wheel_pos * 3, 0)
    elif wheel_pos < 170:
        wheel_pos -= 85
        return (255 - wheel_pos * 3, 0, wheel_pos * 3)
    else:
        wheel_pos -= 170
        return (0, wheel_pos * 3, 255 - wheel_pos * 3)