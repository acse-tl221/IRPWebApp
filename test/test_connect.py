import pytest
import sys
import os
class TestConnect(object):
    """
    Class for testing the ssh connection
    """

    def test_connect(self):
        """ Test the connection """
        CURRENT_DIR = os.path.split(os.path.abspath(__file__))[0]  # 当前目录
        config_path = CURRENT_DIR.rsplit('/', 1)[0]  # 上级目录
        sys.path.append(config_path)
        from utils import connect
        ipName = "43.143.42.56"
        user = "root"
        pwd = "Simulator19980219"
        workDir = "./IRP"
        connection = connect.ConnectionInstance(ipName,user,pwd,workDir)
        res = connection.connectServer()
        connection.scpLogFile()
        connection.closeConnection()

        assert res == True