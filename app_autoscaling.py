import docker
import time
import psutil
import threading

# Docker 클라이언트 초기화
client = docker.from_env()

# Docker 이미지 및 컨테이너 설정
DOCKER_IMAGE = "fog1234/cpu_load_web:3.0"
MAX_CONTAINERS = 3
PORT_RANGE = list(range(12220, 12231))  # 12220~12230

def get_running_containers():
    """현재 실행 중인 Docker 컨테이너 목록을 반환합니다."""
    return client.containers.list(filters={"ancestor": DOCKER_IMAGE})

def add_container(image, port):
    """ 지정된 Docker 이미지를 사용하여 새로운 컨테이너를 추가합니다. """
    client.containers.run(image, detach=True, ports={'5000/tcp': port})
    print(f"컨테이너 추가됨: {image} 포트: {port}")

def monitor_cpu_and_scale():
    """ CPU 사용량을 모니터링하고 필요시 컨테이너를 추가합니다. """
    over_threshold_duration = 0
    threshold = 50.0
    duration_to_trigger_scaling = 5  # 초

    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > threshold:
            over_threshold_duration += 1
        else:
            over_threshold_duration = 0

        if over_threshold_duration >= duration_to_trigger_scaling:
            running_containers = get_running_containers()
            if len(running_containers) < MAX_CONTAINERS:
                available_ports = [port for port in PORT_RANGE if port not in [int(container.attrs['HostConfig']['PortBindings']['5000/tcp'][0]['HostPort']) for container in running_containers]]
                if available_ports:
                    add_container(DOCKER_IMAGE, available_ports[0])
                else:
                    print("사용 가능한 포트가 없습니다.")
            else:
                print("최대 컨테이너 개수에 도달했습니다.")
            over_threshold_duration = 0

        time.sleep(1)

if __name__ == "__main__":
    monitoring_thread = threading.Thread(target=monitor_cpu_and_scale)
    monitoring_thread.start()
