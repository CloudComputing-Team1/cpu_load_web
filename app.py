from flask import Flask, render_template, request
from flask_socketio import SocketIO
import os
import threading
import psutil
import time

app = Flask(__name__)
socketio = SocketIO(app)

cpu_load_threads = []
stop_threads = []
connected_clients = 0
ip_addresses = []

def cpu_load_task(stop_event):
    result = 0
    while not stop_event.is_set():
        for _ in range(1000000):
            result += 1
        time.sleep(0.05)  # 부하를 조절하기 위해 짧은 시간 대기

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
    global connected_clients, cpu_load_threads, stop_threads, ip_addresses
    connected_clients += 1
    ip_address = request.remote_addr
    ip_addresses.append(ip_address)

    if connected_clients <= 3:
        stop_event = threading.Event()
        stop_threads.append(stop_event)
        cpu_thread = threading.Thread(target=cpu_load_task, args=(stop_event,))
        cpu_thread.start()
        cpu_load_threads.append(cpu_thread)
    else:
        socketio.emit('error', {'error': 'Maximum clients connected. Try again later.'})

    socketio.emit('ip_update', {'ips': ip_addresses})

@socketio.on('disconnect')
def handle_disconnect():
    global connected_clients, cpu_load_threads, stop_threads, ip_addresses
    connected_clients -= 1
    ip_address = request.remote_addr
    if ip_address in ip_addresses:
        ip_addresses.remove(ip_address)

    if stop_threads:
        stop_event = stop_threads.pop()
        stop_event.set()
        cpu_thread = cpu_load_threads.pop()
        cpu_thread.join()

    socketio.emit('ip_update', {'ips': ip_addresses})

if __name__ == '__main__':
    monitor_thread = threading.Thread(target=monitor_cpu_load)
    monitor_thread.start()
    
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, debug=True, host='0.0.0.0', port=port)
