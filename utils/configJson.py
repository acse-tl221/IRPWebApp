import json
config_file = {}
config_file["local"] = {"workDir":"./IRP"}
config_file["server"] = {}
config_file["server"]["server1"] = {"ipName":"login.hpc.ic.ac.uk","user":"tl221","pwd":"19980219@Oscar","workDir":"./IRP"}
config_file["server"]["server2"] = {"ipName":"login.hpc.ic.ac.uk","user":"ym321","pwd":"Yjaizj9908!","workDir":"./IRP"}
with open('config.json', 'w') as outfile:
    json.dump(config_file, outfile)