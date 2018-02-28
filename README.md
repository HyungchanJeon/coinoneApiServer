# Coinone Api Server

- Django 1.11 기반 프로젝트입니다.
- Coinone Api를 사용하여 나만의 홈페이지에서 내 정보, 시세조회, 주문 할 수 있습니다.

## 사용법

- `coinoneApiServer/apiApp/views.py` 파일에서 Coinone `TOKEN`, `KEY`를 입력
- `coinoneApiServer/coinoneApiProj/settings.py` 파일에서 `CORS_ORIGIN_WHITELIST`의 client ip를 입력
- Coineone API의 CACHES를 설정할 수 있습니다.
- `coinoneApiServer/coinoneApiProj/settings.py` 파일에서 `CACHES`의 `TIMEOUT` 설정
- Django의 `python manage.py runserver`를 이용하여 실행 

## 테스트 서버

- `http://221.139.32.62:55100/`
