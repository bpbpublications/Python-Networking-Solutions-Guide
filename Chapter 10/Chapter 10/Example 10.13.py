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
