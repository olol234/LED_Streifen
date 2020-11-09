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

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
       pixels.fill((pos * 3, 255 - pos * 3, 0))
    elif pos < 170:
        pos -= 85
       pixels.fill((255 - pos * 3, 0, pos * 3))
    else:
        pos -= 170
        pixels.fill((0, pos * 3, 255 - pos * 3))