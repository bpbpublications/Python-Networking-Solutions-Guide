    def from_multiple_devices():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()
        with open("input/command_list.txt") as r:
            command_list = r.read().splitlines()

        def concurrent(ip):
                device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
                net_connect = Netmiko(**device)
                hostname = net_connect.find_prompt()
                for command in command_list:
                    output = net_connect.send_command(command, strip_command=False)
                    print(f"{hostname} {output}\n")

                    with open(f"output/{ip} logs.txt", "a") as w:
                        w.write(f"{hostname} {output}\n\n")

        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(concurrent, device_list)
