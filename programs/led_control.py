import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 30)

def green():
    pixels.fill((0, 255, 0))