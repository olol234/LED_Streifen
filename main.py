from flask import Flask, render_template, request
import programs.led_control as led
from main.html import value

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/on")
def action():
    led.green()
    return render_template('main.html')

@app.route("/action_page.php")
def action1():
    led.colorpicker(value)
    return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)