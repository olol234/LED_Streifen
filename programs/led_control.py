import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 109)

def green():
    pixels.fill((0,255,0))

def of():
    pixels.fill((0,0,0))

def colorpicker():
    pixels.fill((0,0,0))