import board
import neopixel
import threading

num_pixels = 109
pixels = neopixel.NeoPixel(board.D18, num_pixels)
wheel_execute = False

def green():
    pixels.fill((9,138,236))

def off():
    wheel_execute = False
    pixels.fill((0,0,0))

def colorpicker(color_string):

    color_string = color_string.lstrip('#')
    hlen = len(color_string)
    pixels.fill(tuple(int(color_string[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)))

def wheel_thread(pos):
    while (wheel_execute):
        if pos < 85:
            pixels.fill((pos * 3, 255 - pos * 3, 0))
        elif pos < 170:
            pos -= 85
            pixels.fill((255 - pos * 3, 0, pos * 3))
        else:
            pos -= 170
            pixels.fill((0, pos * 3, 255 - pos * 3))

def wheel(pos):
    wheel_execute = True
    x = threading.Thread(target=wheel_thread, args=(pos,))
    x.start()