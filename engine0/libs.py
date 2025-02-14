import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
from openai import OpenAI
from PyPDF2 import PdfReader
from config import OPEN_AI_API_KEY, KAKAO_TOKEN
import json

client = OpenAI(api_key=OPEN_AI_API_KEY)

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
                # print(f"Downloaded: {file_name}")
                
                return file_name
            else:
                print(f"Failed to download: {file_name}")
                return ""

# PDF에서 텍스트 추출 함수
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print(f"PDF 읽기 중 오류 발생: {e}")
    return text

# ChatGPT API 호출 함수
def ask_chatgpt(text, prompt_template):
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",  # 또는 "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_template.format(text=text)}
        ],
        max_tokens=500,
        temperature=0.7)
        # 응답에서 필요한 내용 추출
        return response.choices[0].message.content
    except Exception as e:
        print(f"ChatGPT 호출 중 오류 발생: {e}")
        return ""

# PDF 분석 및 데이터 추출 함수
def analyze_pdf(pdf_path):
    # PDF에서 텍스트 추출
    pdf_text = extract_text_from_pdf(pdf_path)

    if not pdf_text.strip():
        print("PDF에서 텍스트를 추출하지 못했습니다.")
        return None

    # ChatGPT에 전달할 프롬프트 템플릿
    prompt_template = """
다음은 PDF 문서의 내용입니다. 아래 항목에 맞게 정보를 추출해 주세요. 해당 내용이 없으면 빈칸으로 남겨주세요.
[공고제목 | 지원주체 | 지원자금 | 지원액 | 지원대상 | 융자한도 | 조건 | 신청기간 | 지원지역]

문서 내용:
{text}

결과를 각각 아래 속성에 맞게 JSON 형식으로 반환해 주고, summary에는 해당 내용을 요약해 주세요:
subject: 
entity: 
fund: 
support_amount: 
target: 
loan_limit: 
conditions: 
application_period: 
support_region: 
summary:
"""

    # ChatGPT API 호출
    result = ask_chatgpt(pdf_text, prompt_template)

    return result

# AI 결과를 JSON 형식으로 변환
def formatJson(str):
    # 문자열을 줄 단위로 분리
    lines = str.splitlines()

    # 첫 줄과 마지막 줄을 제거
    modified_lines = lines[1:-1]

    # 남은 줄들을 다시 하나의 문자열로 결합
    modified_string = '\n'.join(modified_lines)

    json_object = json.loads(modified_string)

    return json_object

# 📌 카카오 알림톡 전송 함수
def send_kakao_alert(receiver_phone, message):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {KAKAO_TOKEN}",
        "Content-Type": "application/json",
    }
    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message,
            "link": {"web_url": "https://yourwebsite.com"},  # 필요 시 링크 수정
            "button_title": "자세히 보기",
        })
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

