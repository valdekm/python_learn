import paramiko
plik = open("report.txt","w")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file("/home/valdek/.ssh/id_rsa")

output = ""
errory = ""

print "connecting"
client.connect(hostname="vps1",username="valdek",pkey=key)
print "connected"
commands = ["uname -n","uname -r","systemctl status vsftpd","systemctl status docker","df -h","sudo -i cat /etc/shadow"]

for command in commands:
    print "Executing {}".format( command )
    stdin , stdout, stderr = client.exec_command(command)
    output = output + stdout.read()
    print ("Errors")
    errory = errory + stderr.read()

client.close()

print output
print errory
plik.write(output)

plik.close()
