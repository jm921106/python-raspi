
# embedded
import time
import serial

# class
class RS232:

    # init
    def __init__(self, Baud):

        # 기존
        # self.srl = serial.Serial('/dev/ttyAMA0', baudrate=Baud)
        # 수정
        self.srl = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

        self.arrQueue = []  # 큐 저장소
        self.lock = False   # 큐 잠금 상태

    # send
    def Send (self, data):
        self.srl.write(data)

    # send bytes
    def SendCmd (self, str):
        for ch in str:
            bte = bytearray()
            bte.append(ord(ch))
            self.srl.write(bte)

    # receive
    def Receive (self):
        sno = self.srl.inWaiting()

        if sno == 0:
            return None

        while True:
            time.sleep(0.01)
            sno2 = self.srl.inWaiting()
            if sno == sno2:
                btrcv = self.srl.read(sno)
                return btrcv
            sno = sno2




