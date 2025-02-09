import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import db

def check_file_ext(file_name):
    # Check if the file name is empty or None
    if not file_name:
        return False
    
    # Split the file name by the dot character to get the extension
    parts = file_name.split('.')
    
    # If there is no extension, return False
    if len(parts) < 2:
        return False
    
    # Get the last part of the split list which is the extension
    extension = parts[-1]
    
    # Check if the extension is "pdf"
    return extension.lower() == 'pdf'  

def download_files(url):
    # 웹 페이지 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 'files' 폴더 생성 (존재하지 않는 경우)
    if not os.path.exists('files'):
        os.makedirs('files')

    # 첨부파일 목록 찾기
    file_list = soup.find('div', class_='attached_file_list')
    if file_list:
      ul = file_list.find('ul')
      if ul:
        last_li = ul.find_all('li')[-1]
        links = last_li.find_all('a', class_='icon_download')
        
        for link in links:
            file_url = urljoin(url, link['href'])
            file_name = link.find_previous('div', class_='file_name').text.strip()
            if not check_file_ext(file_name):
              continue
            
            # 파일 다운로드
            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                file_path = os.path.join('files', file_name)
                with open(file_path, 'wb') as file:
                    file.write(file_response.content)
                print(f"Downloaded: {file_name}")
                
                return file_name
            else:
                print(f"Failed to download: {file_name}")
                return ""

# 엑셀 파일 URL
url = "https://www.bizinfo.go.kr/bbs/AS/excelDowload.do?1=1&hashCode=01&schEndAt=N&condition=searchPblancNm&condition1=AND&rescan=N"

# 현재 날짜 (YYYY-MM-DD 형식)
# today = datetime.now().strftime('%Y-%m-%d')


# 현재 날짜 가져오기
today = datetime.today()

# 3일 전 날짜 계산하기
three_days_ago = today - timedelta(days=100)

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
    print(filename)
    db.insert_notice(subject[index], "", department[index], agency[index], start[index], end[index], reg[index], filename)
