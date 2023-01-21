from matplotlib import pyplot as plt
import re
from netmiko import Netmiko
from time import sleep
from datetime import datetime

host = {"host": "10.10.10.1", "username":"admin", "password":"cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}
count = 7
delay = 3
command = "show processes cpu"
cpu_levels = []
time_list = []

net_connect = Netmiko(**host)

for i in range(1,count):
    print(f"Get CPU levels count: {i}")
    output = net_connect.send_command(command)
    time = datetime.now().strftime("%H:%M:%S")
    time_list.append(time)
    sleep(delay)

    cpu_data = re.findall("CPU utilization for five seconds: (\d+)%/", output)
    cpu_levels.append(int(cpu_data[0]))
    print("CPU Level: ",cpu_data[0])

plt.plot(time_list, cpu_levels)
plt.xlabel("Time")
plt.ylabel("CPU Levels in %")
plt.grid(True)
plt.show()
