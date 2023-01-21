from subprocess import Popen, PIPE
from re import findall

hostname = "10.10.10.1"
hops = 1
output = Popen(f"cmd /c tracert -h {hops} {hostname}",stdout=PIPE,encoding="utf-8")
data = ""
for line in output.stdout:
    data = data + "\n" + line.rstrip('\n')
    print(line.rstrip('\n'))

with open (f"Traceroute to {hostname}","w") as wr:
    wr.write(data)

result = findall(f"ms\s+{hostname}",data)

if result:
    print (f"***Traceroute to {hostname} is successfully finished")
else:
    print(f"***Cannot reach {hostname}")     
