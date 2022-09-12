from utils import connect, getConst
import os
import json
import threading
import time

CheckFileName = getConst.ConstManager().getCheckFileName()
configFileName = getConst.ConstManager().getconfigFileName()

class Simulator:
    def __init__(self,target):  #target is the server user selected on the front end
        self.connect = None
        self.target = target
        self.flag = False
        self.ipName = None
        self.user = None
    
    """
    connect to the remote machine and mount the simulator
    """
    def makeConnection(self):
        curPath = os.getcwd()
        with open(os.path.join(curPath,configFileName)) as json_file:
            configInfo = json.load(json_file)
        target_ = self.target
        ipName = configInfo["server"][target_]["ipName"]
        self.ipName = ipName
        user = configInfo["server"][target_]["user"]
        self.user = user
        pwd = configInfo["server"][target_]["pwd"]
        workDir = configInfo["server"][target_]["workDir"]
        self.connect = connect.ConnectionInstance(ipName,user,pwd,workDir)
        self.connect.connectServer()    #ssh connect to the server
        self.updateCheck(False)

    def exeSimulator(self):
        threadMount = threading.Thread(target=self.runTarget).start() #mount the simulator and keep running in child thread

    def runTarget(self):
        print("thread start")
        self.connect.runCommand()
        self.flag = True

    def runLocal(self):
        pass

    """
    get the progress of the simulator by parsing the log file
    """
    def getProgress(self):
        if(self.flag != True):
            print("scp agin")
            self.connect.scpLogFile()
            return False
        else:
            self.connect.scpLogFile()
            self.connect.closeConnection()
            self.updateCheck(True)
            return True

    """
    update the check file
    going to optimize this method to a Thread class, and use lock to synchronize
    """
    def updateCheck(self,isFree):
        lock = threading.Lock()
        target_ = self.target
        curPath = os.getcwd()
        checkInfo = {}
        with open(os.path.join(curPath,CheckFileName),'r') as json_file:
            checkInfo = json.load(json_file)
        lock.acquire()
        checkInfo["server"][target_] = isFree
        with open(os.path.join(curPath,CheckFileName),'w') as json_file:
            json.dump(checkInfo,json_file)
        lock.release()
        
    def getIpName(self):
        return self.ipName+self.user

    def onFinished(self):
        self.flag = True




