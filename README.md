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
