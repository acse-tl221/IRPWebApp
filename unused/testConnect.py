import sys
import os
CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]  # 当前目录
config_path = CURRENT_DIR.rsplit('/', 1)[0]  # 上级目录
sys.path.append(config_path)
from utils import connect
ipName = "login.hpc.ic.ac.uk"
user = "tl221"
pwd = "19980219@Oscar"
workDir = "./IRP"
connection = connect.ConnectionInstance(ipName,user,pwd,workDir)
connection.connectServer()
connection.scpLogFile()
connection.closeConnection()