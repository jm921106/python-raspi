"""
    GPIO.py

    목 적 : GPIO 클래스 (부모)
    단 계 :
    문 제 :
    설 명 :
        매개변수
            arrIO  (list) : 사용하려는 모듈이 IN 모듈인지 OUT 모듈인지
            arrPin (list) : 실행하려는 GPIO. Pin의 위치
    일 자 : 2017.07.26
    작 성 : SuperMoon
    참 조 :

"""

# embedded
import RPi.GPIO as gpio

class GPIO :

    def __init__(self, packet):

        self.packet = packet
        self.arrIO = packet["arrIO"]
        self.arrPin = packet["arrPin"]

        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        for i in range(0, len(self.arrPin)) :
            gpio.setup(self.arrPin[i], getattr(gpio, self.arrIO[i]))

    # GET

    def getArrPin (self) :
        return self.arrPin

    def getArrIO (self) :
        return self.arrIO

    # SET

    def setArrPin (self, arrPin) :
        self.arrPin = arrPin

    def setArrIO (self, arrIO) :
        self.arrIO = arrIO