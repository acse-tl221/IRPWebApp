#dependence
import json
import requests
import pandas as pd
from flask import Flask, request, send_from_directory, render_template,Response, jsonify
import json
#model
from model import CheckResource, MountSimulator, ReadLog
#utils
from utils import connect

"""
hold all the Instances
"""
simulatorInstances = {}

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("moniter.html")


"""
url for check resource
"""
@app.route('/check')
def check():
    instance = CheckResource.CheckResource()
    return instance.CheckAvailable()


"""
url for run the simulator on the remote server or on the local
"""
@app.route('/simulate')
def simulate():
    #identify if simulator has been launched
    isConnected = (int)(request.args.get("isConnected"))
    ifFinished = False
    serverId = request.args.get("id")
    target = serverId
    print(target)
    # double check if the machine is still available now
    curCheck = CheckResource.CheckResource()
    curCheck.CheckAvailable()
    isAvailable = curCheck.isAvailable(target=target)
    if(target in simulatorInstances):
        simulator = simulatorInstances[target]
    else:
        simulator = MountSimulator.Simulator(target)
    # initinalize simulator instance if hasn't connected before, and make the connection
    if isConnected == 0:
        
        if(target == "local"):
            simulator.runLocal()
        else:
            simulator.makeConnection()
            simulator.exeSimulator()
        simulatorInstances[target] = simulator
        isConnected = 1
        res = {"isConnected":isConnected, "isFinished":False}
        return jsonify(res)

    # if the simulator is running, get the progress of the log file
    else:
        ifFinished = simulator.getProgress()
        ipName = simulator.getIpName()
        logThread = ReadLog.LogThread(ipName=ipName)
        logThread.start()
        logContent = logThread.join()
        res = {}
        res["isConnected"] = isConnected
        res["isFinished"] = ifFinished
        res["logContent"] = logContent
        return jsonify(res)

"""
url for track progress when a server is not available
"""
"""
@app.route('/trackProgress')
def track():
    serverId = request.args.get("id")
    target = serverId
    if(target in simulatorInstances):
        simulator = simulatorInstances[target]
    ifFinished = simulator.getProgress()
    ipName = simulator.getIpName()
    logThread = ReadLog.LogThread(ipName=ipName)
    logThread.start()
    logContent = logThread.join()
    res = {}
    res["isFinished"] = ifFinished
    res["logContent"] = logContent
    return jsonify(res)
"""