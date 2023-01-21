from netmiko import Netmiko
from concurrent.futures import ThreadPoolExecutor
from re import findall
from pandas import DataFrame

class config_and_collect_logs:
    def config_collect_logs():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        def concurrent(ip):
            device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
            net_connect = Netmiko(**device)
            hostname = net_connect.find_prompt()
            output = net_connect.send_config_from_file(config_file="input/command_list.txt", strip_command=False)
            print(f"{hostname} {output}\n")

        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(concurrent, device_list)



    def collect_resource_usage():
        memory_total, memory_free, memory_used, cpu_used, host_list = ([] for i in range(5))
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        for ip in device_list:
            device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
            net_connect = Netmiko(**device)
            mem_output = net_connect.send_command("free -m", strip_command=False)
            cpu_output = net_connect.send_command("top -n 1 | grep %Cpu", strip_command=False)
            hostname = findall("@(.*):", net_connect.find_prompt())

            total = findall("Mem:\s+(\d+)", mem_output)
            free = findall("Mem:\s+\d+\s+(\d+)", mem_output)
            used = findall("Mem:\s+\d+\s+\d+\s+(\d+)", mem_output)
            cpu = findall("\d+,\d+", cpu_output)

            memory_total.append(f"{total[0]} MB")
            memory_free.append(f"{free[0]} MB")
            memory_used.append(f"{used[0]} MB")
            cpu_used.append(f"% {cpu[0]}")
            host_list.append(hostname[0])

        df = DataFrame({"Hostname": host_list, "Total Memory": memory_total, "Free Memory": memory_free,
                        "Memory Usage": memory_used, "CPU Usage": cpu_used})
        df.to_excel("output/CPU-Memory Usage.xlsx", index=False)


    def collect_interface_information():
        list_ipv4, list_netmask, list_int, list_hostname, list_int_name = ([] for i in range(5))
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        for ip in device_list:
            device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
            net_connect = Netmiko(**device)
            output = net_connect.send_command("ifconfig")
            hostname = findall("@(.*):", net_connect.find_prompt())
            int_name = findall("(.*): flags", output)

            for interface in int_name:
                output = net_connect.send_command(f"ifconfig -a {interface}")
                ipv4 = findall("inet (.*)  netmask", output)
                netmask = findall("netmask (\d+.\d+.\d+.\d+)", output)
                list_ipv4.append(ipv4[0])
                list_netmask.append(netmask[0])
                list_hostname.append(hostname[0])
                list_int_name.append(interface)

        df = DataFrame({"Hostname": list_hostname, "Interface Name": list_int_name, "IP Address": list_ipv4,
                        "Netmask": list_netmask, })
        df.to_excel("output/Interface Information.xlsx", index=False)


    def package_installation(package):
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        def concurrent(ip):
            device = {"host": ip, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
            net_connect = Netmiko(**device)
            net_connect.send_config_set(f"sudo apt-get install {package} -y")
            output = net_connect.send_command(f"{package} --version")
            hostname = net_connect.find_prompt()
            print(f"{hostname}: {package} --version{output}\n")

        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(concurrent, device_list)