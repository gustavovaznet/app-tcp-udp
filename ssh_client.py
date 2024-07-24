import paramiko

#HOST AND CREDENTIALS
host = "127.0.0.1"
user = "kali"
passwd = "kali"

#CLIENT
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

#COMMANDS
while True:
    stdin, stdout, stderr = client.exec_command(input("Command: "))
    for line in stdout.readlines():
        print(line.strip())

    #ERRORS
    errors = stderr.readlines()
    if errors:
        print(errors)
