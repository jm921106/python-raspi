"""
    processGPIO.py

    목 적 : main.py에 GPIO 관련 모듈을 제공
    설 명 :ㄴ
        main.py에서 GPIO 관련 접근을 요청받았을 때 processGPIO 스크립트에서 GPIO 관련 스크립트 모듈을 사용
        (packet 정보를 받아서 GPIO에 접근 후에 센서 활성화 결과값 반환)
    단 계 : 작성중입니다 :)
    이 슈 :
        rtnPacket의 Boolean 값을 True/False > 'true'/'false'로 사용 (js와 Boolean 형태가 다르기 때문)
    일 자 : 2017.08.03
    작 성 : SuperMoon
    참 조 :

"""

# embedded
import sys, os  # embedded

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path + "/../util")
sys.path.append(path + "/../model")
sys.path.append(path + "/../model/sensor")

# custom
from Packet import Packet

def manageGPIO(packet) :
    rtn = Packet(
        1,          # param
        'false',    # status (string - 'true'/'false')
        None        # result
    )

    # print('excute gpio method') # gpio
    clsName = packet['info']['class']

    # load GPIO class
    mod = __import__('%s' % (clsName), fromlist=[clsName])
    cls = getattr(mod, clsName)(packet['info'])

    # control class
    rtn.result = getattr(cls, packet['info']['control'])()

    rtn.status = 'true'

    return rtn
