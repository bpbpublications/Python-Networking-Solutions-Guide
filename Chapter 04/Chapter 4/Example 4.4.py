from netmiko import Netmiko

device = {                                                     
    "host": "10.10.10.1",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
    "global_delay_factor": 0.1,                          
}

net_connect = Netmiko(**device)

config= ["interface GigabitEthernet0/0", "description TEST"]
command = "show run interface GigabitEthernet0/0"

config_output = net_connect.send_config_set(config)
show_output = net_connect.send_command(command)

net_connect.disconnect()
print(config_output)
print(show_output)