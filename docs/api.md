# API 문서

## 목차

1. [데이터베이스 모듈](#데이터베이스-모듈)
2. [유틸리티 라이브러리](#유틸리티-라이브러리)
3. [데이터베이스 핸들러](#데이터베이스-핸들러)
4. [메인 애플리케이션](#메인-애플리케이션)

---

## 데이터베이스 모듈

### `database.py`

데이터베이스 연결 및 세션 관리를 담당하는 모듈입니다.

#### 함수

##### `init_db()`

데이터베이스 테이블을 생성합니다.

**반환값**: 없음

##### `get_db()`

데이터베이스 세션을 생성하고 관리합니다. FastAPI의 의존성 주입과 함께 사용됩니다.

**반환값**: SQLAlchemy 세션 객체

**사용 예시**:
```python
from database import init_db, get_db

# 데이터베이스 초기화
init_db()

# 세션 사용
db = next(get_db())
# ... 데이터베이스 작업 ...
```

---

## 유틸리티 라이브러리

### `libs.py`

공고 수집, PDF 분석, AI 처리 등의 핵심 유틸리티 함수들을 포함합니다.

#### 함수

##### `check_file_ext(file_name: str) -> bool`

파일 확장자가 PDF인지 확인합니다.

**매개변수**:
- `file_name` (str): 확인할 파일명

**반환값**: PDF 파일이면 True, 아니면 False

##### `download_files(url: str) -> str`

웹 페이지에서 PDF 파일을 다운로드합니다.

**매개변수**:
- `url` (str): 공고 상세 페이지 URL

**반환값**: 다운로드된 파일명, 실패 시 빈 문자열

##### `extract_text_from_pdf(pdf_path: str) -> str`

PDF 파일에서 텍스트를 추출합니다.

**매개변수**:
- `pdf_path` (str): PDF 파일 경로

**반환값**: 추출된 텍스트

##### `ask_chatgpt(text: str, prompt_template: str) -> str`

OpenAI GPT API를 호출하여 텍스트를 분석합니다.

**매개변수**:
- `text` (str): 분석할 텍스트
- `prompt_template` (str): 프롬프트 템플릿

**반환값**: AI 분석 결과

##### `analyze_pdf(pdf_path: str) -> str`

PDF 파일을 분석하여 구조화된 정보를 추출합니다.

**매개변수**:
- `pdf_path` (str): 분석할 PDF 파일 경로

**반환값**: JSON 형식의 분석 결과

##### `formatJson(str: str) -> dict`

AI 분석 결과를 JSON 형식으로 변환합니다.

**매개변수**:
- `str` (str): AI 분석 결과 문자열

**반환값**: 파싱된 JSON 객체

##### `send_kakao_alert(receiver_phone: str, message: str) -> dict`

카카오톡으로 알림 메시지를 전송합니다.

**매개변수**:
- `receiver_phone` (str): 수신자 전화번호
- `message` (str): 전송할 메시지

**반환값**: API 응답

---

## 데이터베이스 핸들러

### `db_handlers.py`

데이터베이스의 CRUD 작업을 수행하는 모듈입니다.

#### Notice 관련 함수

##### `create_notice(db: Session, subject: str, summary: str, department: str, agency: str, filename: str, start_date: datetime, end_date: datetime) -> Notice`

새로운 공고를 데이터베이스에 생성합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `subject` (str): 공고 제목
- `summary` (str): 공고 요약
- `department` (str): 소관 부처
- `agency` (str): 사업 수행 기관
- `filename` (str): 첨부 파일명
- `start_date` (datetime): 시작 날짜
- `end_date` (datetime): 종료 날짜

**반환값**: 생성된 Notice 객체

##### `get_notice(db: Session, notice_id: int) -> Notice`

ID로 공고를 조회합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `notice_id` (int): 공고 ID

**반환값**: Notice 객체 또는 None

##### `update_notice(db: Session, notice_id: int, **kwargs) -> Notice`

공고 정보를 업데이트합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `notice_id` (int): 공고 ID
- `**kwargs`: 업데이트할 필드들

**반환값**: 업데이트된 Notice 객체

##### `delete_notice(db: Session, notice_id: int)`

공고를 삭제합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `notice_id` (int): 삭제할 공고 ID

#### AIResult 관련 함수

##### `create_ai_result(db: Session, notice_id: int, subject: str, summary: str, entity: str, fund: str, support_amount: str, target: str, loan_limit: str, conditions: str, application_period: str, support_region: str) -> AIResult`

AI 분석 결과를 데이터베이스에 저장합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `notice_id` (int): 관련 공고 ID
- 기타 분석 결과 필드들

**반환값**: 생성된 AIResult 객체

##### `get_ai_result(db: Session, ai_result_id: int) -> AIResult`

AI 분석 결과를 ID로 조회합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `ai_result_id` (int): AI 결과 ID

**반환값**: AIResult 객체 또는 None

##### `get_ai_results_from_date(db: Session, base_date: date) -> List[tuple]`

특정 날짜 이후의 AI 분석 결과를 조회합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `base_date` (date): 기준 날짜

**반환값**: (AIResult, Notice) 튜플의 리스트

##### `update_ai_result(db: Session, ai_result_id: int, **kwargs) -> AIResult`

AI 분석 결과를 업데이트합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `ai_result_id` (int): AI 결과 ID
- `**kwargs`: 업데이트할 필드들

**반환값**: 업데이트된 AIResult 객체

##### `delete_ai_result(db: Session, ai_result_id: int)`

AI 분석 결과를 삭제합니다.

**매개변수**:
- `db` (Session): 데이터베이스 세션
- `ai_result_id` (int): 삭제할 AI 결과 ID

---

## 메인 애플리케이션

### `ai_main.py`

공고 수집 및 AI 분석을 수행하는 메인 스크립트입니다.

**사용법**:
```bash
python ai_main.py [기간]
```

**매개변수**:
- `duration` (int): 수집할 기간 (일 단위)

### `sender_main.py`

AI 분석 결과를 카카오톡으로 발송하는 메인 스크립트입니다.

**사용법**:
```bash
python sender_main.py [기간]
```

**매개변수**:
- `duration` (int): 발송할 기간 (일 단위)