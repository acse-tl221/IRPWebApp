import subprocess
connection = subprocess.Popen('sh cmd1.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(connection)
res = connection.stdout.read()
