from flask import Flask, render_template, request
import programs.led_control as led

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/test")
def test():
    led.test()
    return render_template('licht.html')


@app.route("/on")
def on():
    led.green()
    return render_template('licht.html')


@app.route("/off")
def off():
    led.off()
    return render_template('licht.html')


@app.route("/reset")
def reset():
    led.reset()
    return render_template('licht.html')


@app.route("/random")
def random():
    led.random()
    return render_template('licht.html')


@app.route("/Wheel")
def Wheel():
    led.wheel()
    return render_template('licht.html')


@app.route("/fadeRGB")
def fadeRGB():
    led.fadergb()
    return render_template('licht.html')


@app.route("/theaterChase")
def theaterChase():
    led.theaterchase()
    return render_template('licht.html')


@app.route("/colorpicker", methods=['GET', 'POST'])
def colorpicker():
    color_string = request.form['favcolor']
    led.colorpicker(color_string)
    return render_template('licht.html')


@app.route("/licht")
def licht():
    return render_template('licht.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
