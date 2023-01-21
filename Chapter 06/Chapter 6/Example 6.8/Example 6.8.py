from netmiko import Netmiko, file_transfer
import json

def json_device():
    host_list = []
    with open('device_list.json') as json_file:
        data = json.load(json_file)

    for item in data.items():
        host = item[1][0]
        host_list.append(host)
        print(host_list)
    return host_list

host = json_device()

for ip in host:
    net_connect = Netmiko(**ip)
    file_transfer(net_connect,
                  source_file="test.txt",
                  dest_file="test.txt",
                  direction="put",
                  )

    net_connect.disconnect()
