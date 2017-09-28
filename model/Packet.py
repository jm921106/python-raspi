class Packet:

    # init
    def __init__(self, param, status, result):
        self.param = param
        self.status = status
        self.result = result

    def getParam(self):
        return self.param

    def getStatus(self):
        return self.status

    def getResult(self):
        return self.result

    def setParam(self, param):
        self.param = param

    def setStatus(self, status):
        self.status = status

    def setResult(self, result):
        self.result = result

    def returnByteArray(self):
        return {
            "param" : self.param,
            "status" : self.status,
            "result" : self.result
        }

