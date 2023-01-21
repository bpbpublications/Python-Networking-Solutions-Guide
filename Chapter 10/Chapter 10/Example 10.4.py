    def collect_cpu_usage():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        ip_list, cpu_list_5s, cpu_list_1m, cpu_list_5m, cpu_list_risk = ([] for x in range(5))

        for ip in device_list:
            device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
            print(f"\n---Try to Login:{ip}---")
            net_connect = Netmiko(**device)
            output = net_connect.send_command("show processes cpu")

            cpu_5s = findall("CPU utilization for five seconds: (\d+)", output)
            cpu_1m = findall("one minute: (\d+)", output)
            cpu_5m = findall("five minutes: (\d+)", output)

            ip_list.append(ip)
            cpu_list_5s.append(cpu_5s[0] + "%")
            cpu_list_1m.append(cpu_1m[0] + "%")
            cpu_list_5m.append(cpu_5m[0] + "%")

            if int(cpu_5m[0]) > 90:
                cpu_risk = "Fatal CPU Level"
            elif 70 < int(cpu_5m[0]) < 90:
                cpu_risk = "High CPU Level"
            else:
                cpu_risk = "No Risk"

            cpu_list_risk.append(cpu_risk)

        df = DataFrame(
            {"IP Address": ip_list, "CPU Levels for 5 Seconds": cpu_list_5s, "CPU Levels for 1 Minute": cpu_list_1m, "CPU Levels for 5 Minutes": cpu_list_5m, "CPU Risk": cpu_list_risk})
        df.to_excel("output/CPU Levels.xlsx", index=False)
