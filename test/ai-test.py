from openai import OpenAI

client = OpenAI(api_key="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")
from PyPDF2 import PdfReader

# OpenAI API 키 설정

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

결과를 아래 형식으로 반환해 주세요:
공고제목: 
지원주체: 
지원자금: 
지원액: 
지원대상: 
융자한도: 
조건: 
신청기간: 
지원지역: 
"""

    # ChatGPT API 호출
    result = ask_chatgpt(pdf_text, prompt_template)

    return result

# 메인 실행 코드
if __name__ == "__main__":
    pdf_path = "./scrapper/files/2025년 상반기 기술창업 자금지원(융자)사업 공고문.pdf"
    print("PDF 분석 중...")

    result = analyze_pdf(pdf_path)

    if result:
        print("분석 결과:")
        print(result)
