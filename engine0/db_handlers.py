from sqlalchemy.orm import Session
from models import Notice, AIResult
from datetime import date
from typing import List

# Notice CRUD operations
def create_notice(db: Session, subject, summary, department, agency, filename, start_date, end_date):
    new_notice = Notice(subject=subject, summary=summary, department=department, agency=agency,
                        filename=filename, start_date=start_date, end_date=end_date)
    db.add(new_notice)
    db.commit()
    db.refresh(new_notice)
    return new_notice

def get_notice(db: Session, notice_id: int):
    return db.query(Notice).filter(Notice.id == notice_id).first()

def update_notice(db: Session, notice_id: int, **kwargs):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    for key, value in kwargs.items():
        setattr(notice, key, value)
    db.commit()
    db.refresh(notice)
    return notice

def delete_notice(db: Session, notice_id: int):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    db.delete(notice)
    db.commit()

# AIResult CRUD operations
def create_ai_result(db: Session, notice_id, subject, summary, entity, fund, support_amount, target, loan_limit, conditions, application_period, support_region):
    new_ai_result = AIResult(notice_id=notice_id, subject=subject, summary=summary, entity=entity, fund=fund, support_amount=support_amount,
                             target=target, loan_limit=loan_limit, conditions=conditions,
                             application_period=application_period, support_region=support_region)
    db.add(new_ai_result)
    db.commit()
    db.refresh(new_ai_result)
    return new_ai_result

def get_ai_result(db: Session, ai_result_id: int):
    return db.query(AIResult).filter(AIResult.id == ai_result_id).first()

def get_ai_results_from_date(db: Session, base_date: date) -> List[tuple]:
    # return db.query(AIResult).filter(AIResult.created_at > base_date).all()
    return db.query(AIResult, Notice)\
             .join(Notice, AIResult.notice_id == Notice.id)\
             .filter(AIResult.created_at > base_date)\
             .all()

def update_ai_result(db: Session, ai_result_id: int, **kwargs):
    ai_result = db.query(AIResult).filter(AIResult.id == ai_result_id).first()
    for key, value in kwargs.items():
        setattr(ai_result, key, value)
    db.commit()
    db.refresh(ai_result)
    return ai_result

def delete_ai_result(db: Session, ai_result_id: int):
    ai_result = db.query(AIResult).filter(AIResult.id == ai_result_id).first()
    db.delete(ai_result)
    db.commit()
