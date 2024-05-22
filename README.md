# cpu_load_web
cpu 부하를 일으키는 웹

docker hub 주소: https://hub.docker.com/repository/docker/fog1234/cpu_load_web/general
최신 버전: 3.0

docker pull fog1234/cpu_load_web:3.0

docker run -d -p 5000:5000 fog1234/cpu_load_web:3.0

수정 예정1: 사용자가 웹 도커까지 거쳐온 경로(ip 주소 등)을 웹에 표시

수정 예정2: 사용자 3명까지 수용 가능하도록 cpu 과부하 조정
