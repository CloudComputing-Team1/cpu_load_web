# cpu_load_web
cpu 부하를 일으키는 웹

docker hub 주소: https://hub.docker.com/repository/docker/fog1234/cpu_load_web/general
최신 버전: 3.0

DockerHub에서 이미지 가져오기: docker pull fog1234/cpu_load_web:3.0

가져온 이미지를 실행(최상위 root 디렉토리에서 실행하면 하위 디렉토리들까지 이미지 탐색함): docker run -d -p 5000:5000 fog1234/cpu_load_web:3.0

컨테이너만 실행 할 때 포트 동적 할당: docker run -d -P fog1234/cpu_load_web:3.0

Ubuntu 기준 Docker 안 깔려 있을시: https://docs.docker.com/engine/install/ubuntu/ 에서 Install using the apt repository 부분을 따라하면 됨

수정 예정1: 사용자가 웹 도커까지 거쳐온 경로(ip 주소 등)을 웹에 표시 (접속 ip는 표시되는데 그 전 경로 표시는 수정 중)

수정 예정2: 사용자 3명까지 수용 가능하도록 cpu 과부하 조정 (완료)

---
## 오토스케일링 사용설명서

부하를 일으키는 웹을 사용하며 시그널(ex. cpu 사용량 50% 이상 5초 이상 지속) 발생 시 오토스케일링을 수행하는 app_autoscaling.py를 사용하는 방법은 다음과 같습니다. 
(기존에 Docker, Python이 설치되어 있어야 합니다.)

1. **Clone the repository**

    ```sh
    git clone https://github.com/CloudComputing-Team1/cpu_load_web.git
    cd cpu_load_web
    ```

2. **Build the Docker image**

    ```sh
    docker build -t fog1234/cpu_load_web:3.0 .
    ```

3. **Run the Flask application**

    ```sh
    docker run -d -p 5000:5000 fog1234/cpu_load_web:3.0
    ```

4. **Run the auto-scaling script**

    ```sh
    python app_autoscaling.py
    ```

위 방법대로 수행시키면, 시그널에 따라 추가된 컨테이너를 "docker ps" 명령어로 다음과 같이 확인할 수 있습니다. (예시)

    ```sh
    CONTAINER ID   IMAGE                      COMMAND           CREATED          STATUS          PORTS                                         NAMES
    6a017491741e   fog1234/cpu_load_web:3.0   "python app.py"   3 minutes ago    Up 3 minutes    0.0.0.0:12221->5000/tcp, :::12221->5000/tcp   loving_hodgkin
    3ffeab16a5ee   fog1234/cpu_load_web:3.0   "python app.py"   3 minutes ago    Up 3 minutes    0.0.0.0:12220->5000/tcp, :::12220->5000/tcp   inspiring_visvesvaraya
    42e9bb8dd139   fog1234/cpu_load_web:3.0   "python app.py"   18 minutes ago   Up 18 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp     nostalgic_driscoll
    ```
