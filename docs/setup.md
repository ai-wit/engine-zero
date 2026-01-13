# 설치 및 설정 가이드

이 문서는 AI-WIT Engine Zero의 설치 및 설정 과정을 단계별로 안내합니다.

## 📋 사전 요구사항

### 시스템 요구사항

- **운영체제**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.8 이상
- **메모리**: 최소 4GB RAM
- **저장공간**: 최소 1GB 여유 공간

### 외부 서비스 계정

설치 전 다음 서비스들의 계정을 준비해주세요:

1. **OpenAI API 계정**
   - [OpenAI 플랫폼](https://platform.openai.com/)에서 계정 생성
   - API 키 발급 (유료 요금제 필요)

2. **카카오 개발자 계정**
   - [카카오 개발자 센터](https://developers.kakao.com/)에서 앱 생성
   - REST API 키 및 액세스 토큰 발급

3. **데이터베이스**
   - PostgreSQL 또는 SQLite (SQLite는 별도 설치 불필요)

## 🚀 설치 과정

### 1단계: Python 및 pip 설치 확인

```bash
# Python 버전 확인
python --version
# 또는
python3 --version

# pip 버전 확인
pip --version
# 또는
pip3 --version
```

Python 3.8 이상이 설치되어 있지 않다면 [python.org](https://python.org)에서 다운로드하여 설치하세요.

### 2단계: 프로젝트 다운로드

```bash
# Git을 사용하는 경우
git clone https://github.com/ai-wit/engine-zero.git
cd engine-zero

# 또는 ZIP 파일 다운로드 후 압축 해제
cd engine-zero
```

### 3단계: 가상환경 생성 및 활성화 (권장)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 4단계: 의존성 패키지 설치

```bash
pip install -r requirements.txt
```

설치되는 주요 패키지:
- `requests`: HTTP 요청 처리
- `beautifulsoup4`: HTML 파싱
- `pandas`: 데이터 처리
- `sqlalchemy`: 데이터베이스 ORM
- `openai`: OpenAI API 연동
- `PyPDF2`: PDF 텍스트 추출

## ⚙️ 설정 파일 구성

### 1단계: 설정 파일 복사

```bash
cd engine0/src/lib
cp config-dist.ini config.ini
```

### 2단계: API 키 및 토큰 설정

`config.ini` 파일을 텍스트 편집기로 열어 다음 정보를 설정하세요:

```ini
[OPENAI]
api_key = your_openai_api_key_here

[KAKAO]
token = your_kakao_access_token_here

[DATABASE]
url = sqlite:///engine_zero.db  # SQLite 사용시
# 또는 PostgreSQL 사용시:
# url = postgresql://username:password@localhost:5432/engine_zero
```

#### OpenAI API 키 설정

1. [OpenAI 플랫폼](https://platform.openai.com/api-keys) 접속
2. "Create new secret key" 버튼 클릭
3. 생성된 키를 복사하여 `OPENAI.api_key`에 입력

#### 카카오 액세스 토큰 설정

1. [카카오 개발자 센터](https://developers.kakao.com/) 접속
2. 앱 생성 및 설정
3. "카카오 로그인" → "Redirect URI" 설정
4. 액세스 토큰 발급 후 `KAKAO.token`에 입력

#### 데이터베이스 URL 설정

**SQLite (권장 - 별도 설치 불필요)**:
```ini
url = sqlite:///engine_zero.db
```

**PostgreSQL (고급 사용자)**:
```ini
url = postgresql://username:password@localhost:5432/engine_zero
```

### 3단계: 환경 변수 파일 생성 (선택사항)

보안을 위해 `.env` 파일을 생성할 수도 있습니다:

```bash
# 프로젝트 루트 디렉토리에서
touch .env
```

`.env` 파일 내용:
```env
OPENAI_API_KEY=your_openai_api_key_here
KAKAO_TOKEN=your_kakao_access_token_here
DATABASE_URL=sqlite:///engine_zero.db
```

## 🧪 설치 검증

### 1단계: 데이터베이스 초기화 테스트

```bash
cd engine0
python -c "from database import init_db; init_db(); print('데이터베이스 초기화 성공')"
```

### 2단계: OpenAI API 연결 테스트

```bash
cd engine0
python -c "from libs import client; print('OpenAI API 연결 성공')"
```

### 3단계: 기본 기능 테스트

```bash
cd engine0
python ai_main.py --help
python sender_main.py --help
```

## 🔧 문제 해결

### 일반적인 오류와 해결 방법

#### `ModuleNotFoundError`

**증상**: 특정 모듈을 찾을 수 없음

**해결**:
```bash
pip install --upgrade -r requirements.txt
```

#### `OpenAI API 오류`

**증상**: API 키 관련 오류

**해결**:
1. API 키가 올바르게 설정되었는지 확인
2. OpenAI 계정에 잔액이 있는지 확인
3. API 키 권한이 올바른지 확인

#### `Database 연결 오류`

**증상**: 데이터베이스 연결 실패

**해결**:
1. PostgreSQL의 경우 서비스가 실행 중인지 확인
2. 연결 URL이 올바른지 확인
3. 권한 설정 확인

#### `PDF 처리 오류`

**증상**: PDF 파일을 읽을 수 없음

**해결**:
1. PDF 파일이 손상되지 않았는지 확인
2. PyPDF2 버전이 호환되는지 확인
3. 파일 권한 확인

## 📞 지원

설치 과정에서 문제가 발생하면:

1. [GitHub Issues](https://github.com/ai-wit/engine-zero/issues)에서 검색
2. 새로운 이슈 생성 시 다음 정보 포함:
   - Python 버전
   - 운영체제 정보
   - 오류 메시지 전체
   - 실행한 명령어

## 🎯 다음 단계

설치가 완료되면 다음 작업을 수행할 수 있습니다:

1. **기본 테스트 실행**: `python ai_main.py 1`
2. **상세 문서 확인**: `docs/` 폴더의 문서들 참고
3. **커스터마이징**: 필요에 따라 설정 조정