from flask import Flask, render_template, request
import programs.lowlevel as lowlevel

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/on")
def action():
    lowlevel.lowlevel()
    return render_template('main.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)