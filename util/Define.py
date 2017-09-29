"""
    Define.py

    목 적 : protocol 정의 script
    단 계 :
    문 제 :
    일 자 : 2017.07.26
    작 성 : SuperMoon
"""

# GPIO PIN 정리
GPIO_PIN = {
    "17": 11,   # 0
    "18": 12,   # 1
    "27": 13,   # 2
    "22": 15,   # 3
    "23": 16,   # 4
    "24": 18,   # 5
    "25": 22,   # 6
}

def getGpioPin () :
    return GPIO_PIN

# MSG_TYPE 정리
RTN_MSG = {
    '01': 'RTN_SUCCESS', # 01. 성공 결과 값
    '02': 'RTN_FAIL',    # 02. 실패 결과 값
    '03': 'RTN_WAIT'     # 03. 대기 결과 값
}

def getRtnMsg () :
    return RTN_MSG