from netmiko import Netmiko

device1 = {"host": "10.10.10.1", "username": "admin", "password": "cisco",
           "device_type": "cisco_ios", "global_delay_factor": 0.1}
device2 = {"host": "10.10.10.2", "username": "admin", "password": "cisco",
           "device_type": "cisco_ios", "global_delay_factor": 0.1}
device3 = {"host": "10.10.10.3", "username": "admin", "password": "cisco",
           "device_type": "cisco_ios", "global_delay_factor": 0.1}

device_list = [device1, device2, device3]

for host in device_list:
    net_connect = Netmiko(**host)

    config = ["interface g0/0", "description TEST-NETMIKO"]
    command = "show version"

    config_output = net_connect.send_config_set(config)
    show_output = net_connect.send_command(command)

    net_connect.disconnect()
    print("Config is starting from here:", config_output)
    print("Logs are starting from here:", show_output)