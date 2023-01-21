class collect_logs:
    def from_one_device(ip, username, password,command):
        device = { "host": ip, "username": username, "password": password, "device_type": "cisco_ios"}
        net_connect = Netmiko(**device)
        show_output = net_connect.send_command(command)
        print(show_output)
