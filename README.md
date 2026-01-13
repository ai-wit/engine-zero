# AI-WIT Engine Zero

기업마당 공고 수집 및 AI 분석 자동화 시스템

## 📋 프로젝트 개요

AI-WIT Engine Zero는 기업마당의 정부 지원사업 공고를 자동으로 수집하고, AI를 활용하여 공고 내용을 분석하며, 분석 결과를 카카오톡으로 발송하는 시스템입니다.

## ✨ 주요 기능

- **공고 자동 수집**: 기업마당에서 최신 공고 데이터를 실시간으로 수집
- **AI 기반 분석**: GPT-4를 활용한 공고 내용 자동 분석 및 구조화
- **데이터베이스 저장**: 분석 결과를 체계적으로 저장 및 관리
- **알림 발송**: 분석된 정보를 카카오톡으로 자동 발송
- **유연한 기간 설정**: 원하는 기간만큼 과거 데이터를 조회 가능

## 🏗️ 시스템 아키텍처

```
기업마당 → 데이터 수집 → PDF 다운로드 → AI 분석 → DB 저장 → 카카오톡 발송
```

## 🚀 설치 및 설정

### 요구사항

- Python 3.8+
- PostgreSQL 또는 SQLite
- OpenAI API Key
- Kakao API Token

### 설치 방법

1. **의존성 설치**
```bash
pip install -r requirements.txt
```

2. **환경 설정**
```bash
cp engine0/src/lib/config-dist.ini engine0/src/lib/config.ini
```

3. **설정 파일 편집**
`engine0/src/lib/config.ini` 파일을 열어 다음 정보를 설정하세요:
- `OPEN_AI_API_KEY`: OpenAI API 키
- `KAKAO_TOKEN`: 카카오 API 토큰
- `DATABASE_URL`: 데이터베이스 연결 URL

## 📖 사용법

### 공고 수집 및 분석

```bash
cd engine0
python ai_main.py [기간(일)]
```

예시:
```bash
python ai_main.py 7  # 7일간의 공고 수집
```

### 분석 결과 발송

```bash
cd engine0
python sender_main.py [기간(일)]
```

예시:
```bash
python sender_main.py 1  # 1일간의 분석 결과 발송
```

## 📁 프로젝트 구조

```
engine-zero/
├── engine0/                 # 메인 애플리케이션
│   ├── ai_main.py          # 공고 수집 및 AI 분석 메인
│   ├── sender_main.py      # 메시지 발송 메인
│   ├── database.py         # 데이터베이스 설정
│   ├── models.py           # 데이터베이스 모델
│   ├── db_handlers.py      # 데이터베이스 CRUD 핸들러
│   ├── libs.py             # 유틸리티 함수들
│   └── src/
│       └── lib/            # 설정 및 라이브러리
├── data/                   # 데이터 파일
└── docs/                   # 문서 (향후 추가 예정)
```

## 🛠️ 개발 정보

- **언어**: Python 3.8+
- **프레임워크**: SQLAlchemy, OpenAI API, Kakao API
- **데이터베이스**: PostgreSQL/SQLite
- **AI 모델**: GPT-4o-mini

## 📝 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 🤝 기여

기여를 환영합니다! 이슈나 풀 리퀘스트를 통해 참여해주세요.
