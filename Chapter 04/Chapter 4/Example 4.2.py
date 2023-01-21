import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect("10.10.10.1", 22, "admin", "cisco")
 
commands = client.invoke_shell()    
commands.send( "configure terminal \n")
commands.send( "interface gigabitethernet 0/1 \n")
commands.send( "description TEST\n")
commands.send( "do show run interface gigabitethernet 0/1 \n") 
time.sleep(1)   

output = commands.recv(1000000)        
output = output.decode("utf-8")   
print (output)