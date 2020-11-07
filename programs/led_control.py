import board
import neopixel
from flask import Flask, render_template, request

app = Flask(__name__)

pixels = neopixel.NeoPixel(board.D18, 109)

def green():
    pixels.fill((0,255,0))

def colorpicker():
    x = request.form['#ff0000']
    pixels.fill((0,0,0))