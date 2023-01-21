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

        df = DataFrame({"Hostname": host_list, "Total Memory": memory_total, "Free Memory": memory_free, "Memory Usage": memory_used, "CPU Usage": cpu_used})
        df.to_excel("output/CPU-Memory Usage.xlsx", index=False)
