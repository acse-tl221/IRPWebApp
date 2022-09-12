import sys
import os
import threading
import time
CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]  # 当前目录
config_path = CURRENT_DIR.rsplit('/', 1)[0]  # 上级目录
sys.path.append(config_path)
from utils import connect, getConst

logRootPath = getConst.ConstManager().getlogRootPath()

class LogThread(threading.Thread):
    def __init__(self, ipName):
        threading.Thread.__init__(self)
        self.ipName = ipName
        self.tarPath = os.path.join(config_path,logRootPath,self.ipName)
        self.response = {}

  # read log file in the child thread
    def run(self):
        log_list = os.listdir(self.tarPath)
        if(len(log_list)!=0):
            for fileName in log_list:
                if fileName not in self.response:
                    with open(os.path.join(self.tarPath,fileName),'r') as file:
                        content = file.read()
                    self.response[fileName] = content

    def join(self):
        threading.Thread.join(self)
        return self.response


testThread = LogThread("login.hpc.ic.ac.uk")
testThread.start()
print(testThread.join())
