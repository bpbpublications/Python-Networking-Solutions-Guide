from netmiko import Netmiko
device = {
    "host": "10.10.10.1",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios_telnet",
    "global_delay_factor": 0.5
}

net_connect = Netmiko(**device)

command = ["interface g0/0", "description TEST"]
output = net_connect.send_config_set(command)
print(output)