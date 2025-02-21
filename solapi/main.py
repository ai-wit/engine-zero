import json
from src.lib import message

'''
알림톡 발송 예제
한번 요청으로 10,000건의 알림톡 발송이 가능합니다.
'''
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': ['01082334268', '01093425100', '01046934773'],  # array 사용으로 동일한 내용을 여러 수신번호에 전송 가능
                'from': '029302266',
                'kakaoOptions': {
                    'pfId': 'KA01PF250219064640191mt9S9tLdOHO',
                    'templateId': 'KA01TP240110072220677clp0DwzaW23',
                    'disableSms': True,  # 해당 값을 True로 표시할 경우 문자로의 대체 발송이 진행되지 않습니다.
                    'variables': {
                        '#{상점명}': '[기업정보알리미]',
                        '#{구매자명}': '이민호',
                        '#{상품명}': '2025년 관광진흥개발기금 관광사업체 운영자금 특별융자 지원 지침, 500억원 내외, 대·중견기업, 제주특별자치도 소재 사업체 제외, 융자금 신청처: 산업은행 등 14개 은행. 융자금 대출실행은 2025. 4. 24.(목)까지 완료해야 함.',
                    }
                }
            }
            # 한 번의 시도로 최대 10,000건까지 추가 가능
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
