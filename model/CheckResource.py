from operator import truediv
from utils import connect
import os
import json

configFileName = "config.json"
CheckFileName = "check.json"

class CheckResource:
    def __init__(self) -> None:
        self.checkInfo = None
    
    def CheckAvailable(self):
        checkResult = {}
        curPath = os.getcwd()
        with open(os.path.join(curPath,CheckFileName)) as json_file:
            self.checkInfo = json.load(json_file)
        return self.checkInfo
    
    def isAvailable(self,target):
        if target == "local":
            return True
        else:
            return self.checkInfo["server"][target]
    
