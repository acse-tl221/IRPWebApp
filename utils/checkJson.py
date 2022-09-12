import json
check_file = {}
check_file["local"] = True
check_file["server"] = {}
check_file["server"]["server1"] = True
check_file["server"]["server2"] = True
with open('check.json', 'w') as outfile:
    json.dump(check_file, outfile)