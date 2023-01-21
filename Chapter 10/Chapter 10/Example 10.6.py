class configure_device:
    def config_with_netmiko():
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()

        def concurrent(ip):
            device = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
            net_connect = Netmiko(**device)
            output = net_connect.send_config_from_file (config_file="input/command_list.txt", strip_command=False)
            print(output)

        with ThreadPoolExecutor(max_workers=25) as executor:
            executor.map(concurrent, device_list)
