# 기본 도커 이미지로부터 시작합니다.
FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y \
        gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psutil

# 작업 디렉토리를 설정합니다.
WORKDIR C:\Users\admin\dockerfile-folder

# 필요한 파일을 복사합니다.
COPY requirements.txt ./
COPY app.py ./

# 필요한 라이브러리를 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너를 실행할 때 실행될 명령어를 지정합니다.
CMD ["python", "app.py"]
