import paramiko

username = ""
password = ""
hostname = ""
port = 2223

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)

stdin, stdout, stderr = client.exec_command('make all')
result = stderr.readlines()
print (result)

stdin, stdout, stderr = client.exec_command('pwd')
result = stdout.readlines()


print (result)