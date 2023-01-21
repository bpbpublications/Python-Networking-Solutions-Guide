from netmiko import Netmiko
from re import findall
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

host = ["10.10.10.1", "10.10.10.2", "10.10.10.3"]

def collect_cpu(ip):
    device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
    command = "show processes cpu"

    print(f"\n---Try to Login:{ip}---\n")
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    cpu_5s = findall("five seconds: (\d+)",output)
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    if int(cpu_5s[0]) > 90:
        cpu_risk = "Fatal CPU Level"
        with open(f"high_cpu_risk_devices.txt", "a") as w:
            w.write(f"---Time:{time}--- \nIP: {ip} \nCPU:{cpu_5s[0]} \nStatus:{cpu_risk}\n\n")
    elif 70 < int(cpu_5s[0]) < 90:
        cpu_risk = "High CPU Level"
        with open(f"high_cpu_risk_devices.txt", "a") as w:
            w.write(f"---Time:{time}--- \nIP: {ip} \nCPU:{cpu_5s[0]} \nStatus:{cpu_risk}\n\n")
    else:
        cpu_risk = "No Risk"

    with open (f"{ip}_cpu_levels.txt","a") as w:
        w.write(f"---Time:{time}--- \nIP: {ip} \nCPU:{cpu_5s[0]} \nStatus:{cpu_risk}\n\n")

with ThreadPoolExecutor(max_workers=50) as executor:
    result = executor.map(collect_cpu, host)
