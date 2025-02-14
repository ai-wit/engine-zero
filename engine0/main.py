from datetime import datetime, timedelta
import requests
import pandas as pd
from libs import download_files, analyze_pdf, formatJson
from datetime import datetime
from database import init_db, get_db
import db_handlers as crud
import json
import argparse

parser = argparse.ArgumentParser(description='기업마당 공고를 수집하고, AI 분석 결과를 저장합니다.')
parser.add_argument('duration', type=int, help='기간을 입력하세요. (ex: 1, 3, 7)', default=1)
args = parser.parse_args()

# print(f"기간: {args.duration}일")
# exit(0)

# 엑셀 파일 URL
url = "https://www.bizinfo.go.kr/bbs/AS/excelDowload.do?1=1&hashCode=01&schEndAt=N&condition=searchPblancNm&condition1=AND&rescan=N"

# 현재 날짜 (YYYY-MM-DD 형식)
# today = datetime.now().strftime('%Y-%m-%d')

# 현재 날짜 가져오기
today = datetime.today()

# 3일 전 날짜 계산하기
three_days_ago = today - timedelta(days=args.duration)

# YYYY-MM-DD 형식으로 출력하기
base_date = three_days_ago.strftime("%Y-%m-%d")

# 엑셀 파일 다운로드
response = requests.get(url)
with open('downloaded_file.xlsx', 'wb') as f:
    f.write(response.content)

# 엑셀 파일 읽기
df = pd.read_excel('downloaded_file.xlsx')

# [등록일자]가 오늘 날짜인 행 필터링
today_rows = df[df['등록일자'] >= base_date]

# [공고상세URL] 추출
urls = today_rows['공고상세URL'].tolist()
subject = today_rows['공고명'].tolist()
department = today_rows['소관부처'].tolist()
agency = today_rows['사업수행기관'].tolist()
start = today_rows['신청시작일자'].tolist()
end = today_rows['신청종료일자'].tolist()
reg = today_rows['등록일자'].tolist()

# 결과 출력
print(f"기준 날짜({base_date}) 이후 등록된 공고의 상세 URL:")
for index, url in enumerate(urls):
  # print(url)
  filename = download_files(url)
  if filename != None:
    print(subject[index])
    # print(filename)

    init_db()
    db = next(get_db())

    # notice 추가
    new_notice = crud.create_notice(db, subject[index], "", department[index], agency[index], filename, datetime.now(), datetime.now())
    print(f"생성된 공지사항 ID: {new_notice.id}")

    pdf_path = f"files/{filename}"
    result = analyze_pdf(pdf_path)

    if result:
        # 결과 출력
        print("분석 결과:")
        json_result = formatJson(result)
        # print(json_result["subject"])
        print(json_result)
        
        # AI 결과 추가
        new_ai_result = crud.create_ai_result(db, new_notice.id, json_result["subject"], json_result["summary"], json_result["entity"], json_result["fund"], json_result["support_amount"], json_result["target"], json_result["loan_limit"], json_result["conditions"], json_result["application_period"], json_result["support_region"])
        print(f"생성된 AI 결과 ID: {new_ai_result.id}")
