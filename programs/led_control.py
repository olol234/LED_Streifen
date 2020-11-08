import board
import neopixel


num_pixels = 109
pixels = neopixel.NeoPixel(board.D18, num_pixels)

def green():
    pixels.fill((9,138,236))

def off():
    pixels.fill((0,0,0))

def colorpicker(color_string):

    color_string = color_string.lstrip('#')
    hlen = len(color_string)
    pixels.fill(tuple(int(color_string[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)))

