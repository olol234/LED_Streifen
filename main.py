from flask import Flask, render_template, request
import programs.led_control as led



app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/on")
def on():
    led.green()
    return render_template('main.html')

@app.route("/off")
def off():
    led.off()
    return render_template('main.html')

@app.route("/reset")
def reset():
    led.reset()
    return render_template('main.html')

@app.route("/random")
def random():
    led.random()
    return render_template('main.html')

@app.route("/Wheel")
def Wheel():
    led.wheel()
    return render_template('main.html')

@app.route("/FadeRGB")
def FadeRGB():
    led.fadergb()
    return render_template('main.html')


@app.route("/colorpicker", methods=['GET','POST'])
def colorpicker():
    color_string = request.form['favcolor']
    led.colorpicker(color_string)
    return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

