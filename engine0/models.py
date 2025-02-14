from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Notice(Base):
    __tablename__ = 'Notice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String(255), nullable=False)
    summary = Column(String(255))
    department = Column(String(255))
    agency = Column(String(255))
    filename = Column(String(255))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AIResult(Base):
    __tablename__ = 'AI_Result'
    id = Column(Integer, primary_key=True, autoincrement=True)
    notice_id = Column(Integer)
    subject = Column(String(255), nullable=False)
    summary = Column(String(255))
    entity = Column(String(255))
    fund = Column(String(255))
    support_amount = Column(String(255))
    target = Column(String(255))
    loan_limit = Column(String(255))
    conditions = Column(String(255))
    application_period = Column(String(255))
    support_region = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
