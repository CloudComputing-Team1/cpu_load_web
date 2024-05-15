from flask import Flask
import psutil
import time

app = Flask(__name__)

@app.route('/')
def index():
    result = 0
    # 최대 CPU 사용량을 정의합니다. 이 값은 CPU의 총 개수에 따라 조정될 수 있습니다.
    MAX_CPU_PERCENTAGE = 50
    
    while True:
        # 현재 CPU 사용량을 가져옵니다.
        cpu_percent = psutil.cpu_percent()
        
        # CPU 사용량이 최대값을 넘어가면 while 루프를 빠져나갑니다.
        if cpu_percent > MAX_CPU_PERCENTAGE:
            break
        
        # CPU 부하를 일으키는 작업을 수행합니다.
        # 간단한 계산을 여러 번 반복하여 CPU 사용량을 높입니다.
        result = result + 1

        time.sleep(0.001)

    
    return f'CPU 부하가 50%를 넘었습니다. {cpu_percent}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

