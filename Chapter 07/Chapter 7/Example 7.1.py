from netmiko import Netmiko, file_transfer
from re import findall
import os

device = {"host": "10.10.10.1", "username": "admin", "password": "cisco", "device_type": "cisco_ios", "global_delay_factor": 0.1 }
filename = "universalk9.17.08.01.bin"
set_software = [f"boot system {file_sys}{filename}","config-register 0x2102"]
local_filesize = os.path.getsize(filename)

net_connect = Netmiko(**device)
file_transfer(net_connect,
              source_file=filename,
              dest_file= filename,
              direction="put",
              )

output = net_connect.send_command(f"dir | include {filename}")
remote_filesize = findall("\d+",output)
net_connect.send_config_set(set_software)
output = net_connect.send_command(f"show run | include {filename}")
boot_set = findall(set_software[0],output)
net_connect.send_command(f"wr")

if str(local_filesize) == remote_filesize[1] and set_software[0] == boot_set[0]:
    print("File is uploaded and set to boot successfully")
    net_connect.send_command("reload", expect_string="Proceed with reload")
    net_connect.send_command_timing("\n", delay_factor=1)

else:
    print("File upload or setting software as boot is failed")

net_connect.disconnect()
