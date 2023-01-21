    def collect_device_info():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        ip_list, version_list, model_list, vendor_list, hostname_list = ([] for i in range(5))

        for ip in device_list:
            device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
            print(f"\n---Try to Login:{ip}---\n")
            net_connect = Netmiko(**device)
            output = net_connect.send_command("show version")

            version = findall("Version (.*),", output)
            model = findall("Cisco (.*)\(revision", output)
            vendor = findall("Cisco", output)
            hostname = findall("(.*)#", net_connect.find_prompt())

            ip_list.append(ip)
