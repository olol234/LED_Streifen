from flask import Flask, render_template, request
import programs.led_control as led


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/on")
def action():
    led.green()
    return render_template('main.html')

@app.route("/off")
def action2():
    led.off()
    return render_template('main.html')

@app.route("/wheel")
def action2():
    led.off()
    return render_template('main.html')

@app.route("/colorpicker", methods=['GET','POST'])
def action1():
    color_string = request.form['favcolor']
    led.colorpicker(color_string)
    return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)