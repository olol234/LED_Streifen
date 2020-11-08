from flask import Flask, render_template, request
import programs.led_control as led


app = Flask(__name__)

x = request.form['']
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

@app.route("/colorpicker", methods=['POST'])
def action1():
    color_string= request.form['favcolor']
    print(color_string)
    led.colorpicker()
    return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)