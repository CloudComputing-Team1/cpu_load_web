from flask import Flask, render_template
from flask_socketio import SocketIO
import psutil
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

cpu_load_thread = None
stop_thread = False
connected_clients = 0

def increase_cpu_load():
    global stop_thread
    result = 0
    while not stop_thread:
        for _ in range(1000000):
            result += 1

def monitor_cpu_load():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        socketio.emit('cpu_update', {'cpu': cpu_percent})
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    global cpu_load_thread, stop_thread, connected_clients
    connected_clients += 1
    stop_thread = False

    if connected_clients == 1:
        cpu_load_thread = threading.Thread(target=increase_cpu_load)
        cpu_load_thread.start()

@socketio.on('disconnect')
def handle_disconnect():
    global stop_thread, connected_clients
    connected_clients -= 1
    if connected_clients == 0:
        stop_thread = True

if __name__ == '__main__':
    monitor_thread = threading.Thread(target=monitor_cpu_load)
    monitor_thread.start()
    socketio.run(app, debug=True, host='0.0.0.0')

