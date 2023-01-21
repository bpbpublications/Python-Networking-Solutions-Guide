import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect("10.10.10.1", 22, "admin", "cisco")
 
commands = client.invoke_shell()    
commands.send("show version \n") 
time.sleep(1)   

output = commands.recv(1000000)        
output = output.decode("utf-8")   
print (output)