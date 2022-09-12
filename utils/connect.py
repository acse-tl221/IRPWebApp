from sys import stdout
from stat import S_ISDIR, S_ISREG
from utils import getConst
import paramiko
import os

#the root of all log file
logRootPath = getConst.ConstManager().getlogRootPath()
srcLogPath = getConst.ConstManager().getsrcLogPath()


class ConnectionInstance:
    def __init__(self, server, username, password,workDir):
        self.username = username
        self.password = password
        self.server = server
        self.ssh_client = paramiko.SSHClient()
        self.sftp = None
        self.workDir = workDir
        self.logDir = srcLogPath
    """
    safe ssh connect to the server
    """
    def connectServer(self):
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname = self.server, username =self.username, password = self.password)
        self.sftp = self.ssh_client.open_sftp()
        return True

    def runCommand(self):
        cdToWorkDir = (" ".join(["cd", self.workDir]))  #work directory of the machine
        compileCmd = getConst.ConstManager().getcompileCmd()   #command to compile c++(can be deleted if compiled isn't required)
        runCmd = getConst.ConstManager().getrunCmd()  #command to run the simulator
        exitCmd = getConst.ConstManager().getexitCmd()    #close the session
        commandExe = ("; ".join([cdToWorkDir,compileCmd,runCmd,exitCmd]))
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh_client.exec_command(commandExe)
        ssh_stdout.readlines()

    """
    scp log file
    """
    def scpLogFile(self):
        srcPath = os.path.join(self.workDir,self.logDir)
        destPath = os.path.join(logRootPath,self.server+self.username)
        if not os.path.isdir(destPath):
            os.makedirs(destPath, exist_ok=True)
        else:
            dest_list = os.listdir(destPath)
            if len(dest_list) != 0:
                for item in dest_list:
                    os.remove(os.path.join(destPath,item))
        self.scp_folder(srcPath,destPath)

    """
    recursive method to scp folder
    """
    def scp_folder(self,path, dest):
        item_list = self.sftp.listdir_attr(path)
        dest = str(dest)
        if not os.path.isdir(dest):
            os.makedirs(dest, exist_ok=True)
        for item in item_list:
            mode = item.st_mode
            src_path = os.path.join(path,item.filename)
            dest_path = os.path.join(dest,item.filename)
            if S_ISDIR(mode):
                self.scp_folder(src_path, dest_path)
            else:
                self.sftp.get(src_path, dest_path)

    def closeConnection(self):
        if(self.ssh_client):
            self.ssh_client.close()
            self.sftp.close()
