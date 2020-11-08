import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 109)

def green():
    pixels.fill((9,138,236))

def off():
    pixels.fill((#ff0000))

def colorpicker():
    pixels.fill(())