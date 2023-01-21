from netmiko import Netmiko
import re
from pandas import DataFrame
device1 = {"host": "10.10.10.1", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}
device2 = {"host": "10.10.10.2", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}
device3 = {"host": "10.10.10.3", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1}
host = [device1, device2, device3]
command = "show processes cpu"
ip_list, cpu_list_5s, cpu_list_1m, cpu_list_5m, cpu_list_risk = ([] for x in range(5))

for ip in host:
    try:
        print(f"\n---Try to Login:{ip['host']}---\n")
        net_connect = Netmiko(**ip)
        output = net_connect.send_command(command)

        cpu_5s = re.findall("CPU utilization for five seconds: (\d+)",output)
        cpu_1m = re.findall("one minute: (\d+)",output)
        cpu_5m = re.findall("five minutes: (\d+)",output)

        ip_list.append(ip['host'])
        cpu_list_5s.append(cpu_5s[0]+"%")
        cpu_list_1m.append(cpu_1m[0] + "%")
        cpu_list_5m.append(cpu_5m[0] + "%")

        if int(cpu_5m[0]) > 90:
            cpu_risk = "Fatal CPU Level"
        elif 70< int(cpu_5m[0]) <90:
            cpu_risk = "High CPU Level"
        else:
            cpu_risk = "No Risk"

        cpu_list_risk.append(cpu_risk)

        df=DataFrame({"IP Address":ip_list,"CPU Levels for 5 Seconds": cpu_list_5s,
                       "CPU Levels for 1 Minute":cpu_list_1m,
                       "CPU Levels for 5 Minutes":cpu_list_5m,"CPU Risk":cpu_list_risk})
        df.to_excel("CPU Levels.xlsx",index=False)


    except:
        print(f"***Cannot Login to {ip['host']}")