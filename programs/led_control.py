import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 109)

def green(color):
    pixels.fill((0,255,0))

def colourpicker(color):
    pixels.fill(color)