class ConstManager:
    def __init__(self) -> None:
        self.logRootPath = "logFile" #name of the copied logFile folder in this machine
        self.srcLogPath = "log" #name of the log directory on the remote machine
        self.CheckFileName = "check.json"   #name of the check file
        self.configFileName = "config.json" #name of the config file
        self.compileCmd = "g++ -std=c++0x  -o dummy dummy.cpp"   #command to compile c++(can be deleted if compiled isn't required)
        self.runCmd = "./dummy"  #command to run the simulator
        self.exitCmd = "exit"    #command to close the session

    def getlogRootPath(self):
        return self.logRootPath
    
    def getsrcLogPath(self):
        return self.srcLogPath
    
    def getCheckFileName(self):
        return self.CheckFileName
    
    def getconfigFileName(self):
        return self.configFileName
    
    def getcompileCmd(self):
        return self.compileCmd
    
    def getrunCmd(self):
        return self.runCmd
    
    def getexitCmd(self):
        return self.exitCmd
    