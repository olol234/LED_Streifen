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

@app.route("/action_page.php")
def action1():
    x = request.from['#ff0000']
    led.colorpicker(x)
    return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)