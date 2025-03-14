from datetime import datetime, timedelta
from datetime import datetime
from database import init_db, get_db
import db_handlers as crud
import argparse
from models import AIResult
from typing import List
from src.lib import message
import json


parser = argparse.ArgumentParser(description='메시지를 발송합니다.')
parser.add_argument('duration', type=int, help='기간을 입력하세요. (ex: 1, 3, 7)', default=1)
args = parser.parse_args()

def print_ai_results(results: List[AIResult]):
    for result in results:
        print(f"ID: {result.id}, Subject: {result.subject}, Created At: {result.created_at}")

def makeMessage(content, recievers):
    data = {
        'messages': [
            {
                'to': recievers,  # array 사용으로 동일한 내용을 여러 수신번호에 전송 가능
                'from': '029302266',
                'kakaoOptions': {
                    'pfId': 'KA01PF250219064640191mt9S9tLdOHO',
                    'templateId': 'KA01TP250307024129121NffSDtLrk8Y',
                    'disableSms': True,  # 해당 값을 True로 표시할 경우 문자로의 대체 발송이 진행되지 않습니다.
                    'variables': content
                }
            }
            # 한 번의 시도로 최대 10,000건까지 추가 가능
        ]
    }
    return data

def sendMessage(results: List[AIResult]):

    for ai_result, notice in results:
        base_date = ai_result.created_at.strftime("%Y-%m-%d")
        content = {
            '#{날짜}': base_date,
            '#{공고제목}': ai_result.subject,
            '#{소관부처}': notice.department,
            '#{지원자금}': ai_result.fund,
            '#{지원규모}': ai_result.support_amount,
            '#{지원대상}': ai_result.target,
            '#{지원한도}': ai_result.loan_limit,
            '#{지원조건}': ai_result.conditions,
            '#{신청기간}': ai_result.application_period,
        }
        recievers = ['01082334268', '01093425100', '01046934773']
        data = makeMessage(content, recievers)
        print(data)
        
        res = message.send_many(data)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))


# print(f"기간: {args.duration}일")
# exit(0)

# 현재 날짜 (YYYY-MM-DD 형식)
# today = datetime.now().strftime('%Y-%m-%d')

# 현재 날짜 가져오기
today = datetime.today()

# n일 전 날짜 계산하기
n_days_ago = today - timedelta(days=args.duration)

# YYYY-MM-DD 형식으로 출력하기
base_date = n_days_ago.strftime("%Y-%m-%d")

init_db()
db = next(get_db())

results = crud.get_ai_results_from_date(db, base_date)

# 결과 출력
if results:
    print("Send Message:")
    sendMessage(results)
else:
    print("No AI results found.")
