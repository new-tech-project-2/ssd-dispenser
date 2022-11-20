![header](https://capsule-render.vercel.app/api?type=rounded&color=auto&section=header&text="SSD%20Dispenser"&fontSize=70)
# Introduction
![python](https://img.shields.io/badge/python-3.9-blue)
![py532](https://img.shields.io/badge/-py532lib-blue)
![socketio](https://img.shields.io/badge/-socketio-random)

`SSD(Smart Soju Dispenser)` 프로젝트의 디스펜서 내 라즈베리파이에 사용되는 레포지토리입니다.

### 👉 연계 Backend 서버
> https://github.com/new-tech-project-2/ssd-backend

### 👉 연계 Frontend 서버
> https://github.com/new-tech-project-2/ssd-frontend

# Execution
```
python3 my_websocket.py
```
# how-to-use
* my_websocket을 실행합니다.
* nfc 모듈에 nfc 태그를 접촉할 시 backend 서버에 정보를 전송합니다.
* socket을 통해 backend 서버에서 전송받은 디스펜서 모드 정보를 업데이트 합니다.
![Footer](https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=footer)
