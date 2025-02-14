import pyautogui
import time

def send_kakao_message(chat_room, message):
    # 카카오톡 앱 활성화 (Spotlight 검색 사용)
    pyautogui.hotkey('command', 'space')
    time.sleep(0.5)
    pyautogui.write('카카오톡')
    time.sleep(0.5)
    pyautogui.press('return')
    time.sleep(2)  # 카카오톡이 열릴 때까지 대기

    # 새 채팅방 열기
    pyautogui.hotkey('command', 'n')
    time.sleep(1)

    # 채팅방 이름 입력
    pyautogui.write(chat_room)
    time.sleep(0.5)
    pyautogui.press('return')
    time.sleep(1)

    # 메시지 입력 및 전송
    pyautogui.write(message)
    time.sleep(0.5)
    pyautogui.press('return')

    print(f"메시지 '{message}'를 '{chat_room}'에 전송했습니다.")

# 사용 예시
chat_room = "조진의대표님"
message = "안녕하세요, 이것은 자동으로 보내는 메시지입니다."

send_kakao_message(chat_room, message)
