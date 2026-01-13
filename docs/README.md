# 문서 디렉토리

AI-WIT Engine Zero 프로젝트의 문서들을 포함하는 디렉토리입니다.

## 📚 문서 목록

### [README.md](../README.md)
프로젝트의 기본적인 소개, 설치 방법, 사용법을 설명합니다.

### [api.md](./api.md)
주요 모듈들의 API 문서를 제공합니다.
- `database.py`: 데이터베이스 연결 및 세션 관리
- `libs.py`: 유틸리티 함수들 (PDF 처리, AI 분석, 메시징 등)
- `db_handlers.py`: 데이터베이스 CRUD 작업
- 메인 애플리케이션 모듈 설명

### [setup.md](./setup.md)
프로젝트의 상세한 설치 및 설정 과정을 안내합니다.
- 시스템 요구사항
- 의존성 패키지 설치
- 설정 파일 구성
- 문제 해결 가이드

### [architecture.md](./architecture.md)
시스템의 전체적인 아키텍처를 설명합니다.
- 컴포넌트 구조 및 데이터 흐름
- 설계 원칙 (SOLID)
- 기술 스택
- 확장성 및 보안 고려사항

## 🎯 문서 이용 가이드

### 처음 사용자라면
1. [README.md](../README.md)로 프로젝트 개요 파악
2. [setup.md](./setup.md)로 설치 및 설정 진행
3. [architecture.md](./architecture.md)로 시스템 이해

### 개발자라면
1. [api.md](./api.md)로 코드 구조 및 API 이해
2. [architecture.md](./architecture.md)로 설계 원칙 학습
3. 기존 코드를 참고하여 기능 확장

## 📝 문서 기여

문서 개선이나 추가가 필요한 경우:
1. 해당 문서를 수정하거나 새 문서 생성
2. 변경사항을 커밋하여 PR 생성
3. 다른 개발자들의 리뷰 받기

## 🔄 업데이트 주기

- **주요 릴리스 시**: README.md 및 setup.md 업데이트
- **API 변경 시**: api.md 업데이트
- **아키텍처 변경 시**: architecture.md 업데이트

## 📞 문의

문서와 관련된 질문이나 개선 제안은 [GitHub Issues](https://github.com/ai-wit/engine-zero/issues)로 등록해주세요.