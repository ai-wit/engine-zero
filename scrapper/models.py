from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Base 클래스 생성
Base = declarative_base()

# Notice 테이블 정의
class Notice(Base):
    __tablename__ = 'notice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String(255), nullable=False)
    summary = Column(String(500), nullable=True)
    department = Column(String(100), nullable=True)
    agency = Column(String(100), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    reg_date = Column(Date, nullable=True)
    filename = Column(String(255), nullable=True)
    status = Column(String(1), nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)