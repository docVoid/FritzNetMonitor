from flask import Flask, render_template
from fritzreader import get_connected_devices

app = Flask(__name__)

@app.route('/')
def dashboard():
    devices = get_connected_devices()
    print(devices)
    return render_template('dashboard.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)
