import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 109)

def green():
    pixels.fill((0,255,0))

def colorpicker(color):
    x = request.form['#ff0000']
    pixels.fill((x))