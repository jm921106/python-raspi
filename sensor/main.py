"""
    main.py

    목 적 : Sensor의 Main Script
    설 명 : Serial 통신에서 전달 받은 매개변수를 이용해서 라즈베리파이의 센서를 동작 시키는 스크립트
    단 계 :
    이 슈 :
        Electron에 True(Boolean)를 Send 하지 말 것
    일 자 : 2017.07.26
    작 성 : SuperMoon
    참 조 :
"""

# embedded
import sys, os  # embedded
import ast      # str > dict

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path + "/../util")
sys.path.append(path + "/../model")
sys.path.append(path + "/../model/sensor")

# custom
from RS232 import RS232
from Packet import Packet
import Define
import util

# TODO console
print ('sensor/main.py call')

# arg1 = sys.argv[0] # file
strPacket = util.rollbackStr(sys.argv[1])
packet = ast.literal_eval(strPacket)

# connect type
if packet['prop'] == 'gpio':
    import processGPIO
    rtnPacket = processGPIO.manageGPIO(packet)

    # # print('excute gpio method') # gpio
    # clsName = packet['info']['class']
    #
    # # load GPIO class
    # mod = __import__('%s' % (clsName), fromlist=[clsName])
    # cls = getattr(mod, clsName)(packet['info'])

# Serial 객체를 새로 만듬
Serial = RS232(115200)
Serial.SendCmd(str(rtnPacket.returnByteArray()))
print('complete!')




