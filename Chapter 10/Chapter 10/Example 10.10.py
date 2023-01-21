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
