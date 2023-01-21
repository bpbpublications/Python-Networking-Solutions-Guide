from netmiko import Netmiko

host = "192.168.163.135"
device = {"host": host, "username": "ubuntu", "password": "ubuntu", "device_type": "linux", "secret": "ubuntu"}
package = "htop"

net_connect = Netmiko(**device)
output = net_connect.send_config_set(f"apt-get install {package} -y")
print(output)

output = net_connect.send_command(f"{package} --version")
print(f"{host}: {package} --version{output}\n")
net_connect.disconnect()
