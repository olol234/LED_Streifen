import board
import neopixel
import threading
import time
import random

num_pixels = 109
pixels = neopixel.NeoPixel(board.D18, num_pixels)

wheel_execute = False
fadergb_execute = False
theaterchase_ecexute = False

def green():
    pixels.fill((9,138,236))


def off():
    pixels.fill((0,0,0))

def reset():
    global wheel_execute
    global fadergb_execute
    global theaterchase_ecexute
    wheel_execute = False
    fadergb_execute = False
    theaterchase_ecexute = False
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

            for j in range(255, 0, -1):
                if i == 0:
                    pixels.fill((j, 0, 0))
                elif i == 1:
                    pixels.fill((0, j, 0))
                elif i == 2:
                    pixels.fill((0, 0, j))


def fadergb():
    global fadergb_execute
    if not fadergb_execute:
        fadergb_execute = True
        x = threading.Thread(target=fadergb_thread, args=())
        x.start()

def theaterchase():
    global theaterchase_ecexute
    if not theaterchase_ecexute:
        theaterchase_ecexute = True
        x = threading.Thread(target=theaterchase_thread, args=())
        x.start()

def theaterchase_thread():
    global theaterchase_ecexute
    while (theaterchase_ecexute):
        for i in range(num_pixels):
            if i %3 == 0:
                pixels.setPixelColor(i,(255,0,0))
            else:
                pixels.setPixelColor(i,(0,0,0))
        pixels.show()
