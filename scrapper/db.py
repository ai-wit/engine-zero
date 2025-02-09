from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Notice

# Base 클래스 생성
Base = declarative_base()

# 데이터베이스 연결 설정 (MariaDB)
DATABASE_URL = "mariadb+mariadbconnector://p333:333333@52.91.4.160:3306/project333"

engine = create_engine(DATABASE_URL, echo=True)

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

# 테이블 생성 (필요 시 실행)
Base.metadata.create_all(engine)

# 데이터 삽입 예제
def insert_notice(_subject, _summary, _department, _agency, _start_date, _end_date, _reg_date, _filename):
    try:
        # Notice 객체 생성
        new_notice = Notice(
            subject=_subject,
            summary=_summary,
            department=_department,
            agency=_agency,
            start_date=_start_date,
            end_date=_end_date,
            reg_date=_reg_date,
            filename=_filename,
            status="0"
        )
        
        # 세션에 추가 및 커밋
        session.add(new_notice)
        session.commit()
        print("데이터가 성공적으로 삽입되었습니다!")
    except Exception as e:
        # 오류 발생 시 롤백
        session.rollback()
        print(f"오류 발생: {e}")
    finally:
        # 세션 종료
        session.close()

# 함수 호출
if __name__ == "__main__":
    insert_notice("제목", "요약", "ex.pdf")
