import board
import neopixel


num_pixels = 109
pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)

def green():
    pixels.fill((9,138,236))

def off():
    pixels.fill((0,0,0))

def colorpicker(color_string):

    color_string = color_string.lstrip('#')
    hlen = len(color_string)
    pixels.fill(tuple(int(color_string[i:i + hlen // 3], 16) for i in range(0, hlen, hlen // 3)))

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        pixels.fill(0, 0, 0)
    if pos < 85:
        pixels.fill(255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        pixels.fill(0, 255 - pos * 3, pos * 3)

    pos -= 170
    pixels.fill(pos * 3, 0, 255 - pos * 3)