from netmiko import Netmiko, file_transfer
import json
from datetime import datetime

def json_device():
    host_list = []
    with open('device_list.json') as json_file:
        data = json.load(json_file)

    for item in data.items():
        host = item[1][0]
        host_list.append(host)
    return host_list

host = json_device()

for ip in host:
    net_connect = Netmiko(**ip)
    print(f"\n----Try to login: {ip['host']}---\n")
    save = net_connect.send_command("wr")
    print(save)
    time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    hostname = net_connect.find_prompt()[:-1]

    file_transfer(net_connect,
                  source_file="startup-config",
                  dest_file=f"{hostname} backup_config {time}.cfg",
                  direction="get",
                  file_system="nvram:",
                  overwrite_file=True
                  )

    net_connect.disconnect()
