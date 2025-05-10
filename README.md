# FastAPI 프로젝트

FastAPI 기반의 웹 애플리케이션 프로젝트입니다.

## 설치 방법

### 로컬 환경에서 실행

1. 가상환경 생성:
```bash
python -m venv .venv
```

2. 가상환경 활성화:
- Windows:
```bash
.venv\Scripts\activate
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

3. 의존성 패키지 설치:
```bash
pip install -r requirements.txt
```

### Docker를 사용하여 실행

1. Docker와 Docker Compose가 설치되어 있어야 합니다.

2. Docker 컨테이너 빌드 및 실행:
```bash
# 컨테이너 빌드 및 실행
docker-compose up --build

# 백그라운드에서 실행
docker-compose up -d --build

# 컨테이너 중지
docker-compose down

# 컨테이너와 이미지 삭제
docker-compose down --rmi all

# 볼륨까지 모두 삭제
docker-compose down --rmi all -v
```

## 애플리케이션 실행

### 로컬 환경
개발 모드로 애플리케이션을 실행하려면:

```bash
uvicorn main:app --reload
```

### Docker 환경
Docker Compose로 실행하면 자동으로 서버가 시작됩니다.

API는 http://localhost:8000 에서 접근 가능합니다.

API 문서는 다음 주소에서 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 개발 정보

- `main.py`: 메인 애플리케이션 파일
- `requirements.txt`: 프로젝트 의존성 패키지 목록
- `.env`: 환경 변수 설정 파일 (이 파일을 생성하고 환경 변수를 추가하세요)
- `docker-compose.yml`: Docker 서비스 설정 파일
- `Dockerfile`: Docker 이미지 빌드 설정 파일 