from netmiko import Netmiko, file_transfer

device = {"host": "10.10.10.1", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1 }

net_connect = Netmiko(**device)

file_transfer(net_connect, 
              source_file="test.txt", 
              dest_file="test10.txt", 
              direction="put")

net_connect.disconnect()
