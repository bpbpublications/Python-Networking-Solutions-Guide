from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
import nornir_netmiko

commands = ["show arp", "show ip interface brief", "show interface description"]

connect = InitNornir()
for comm in commands:
    result = connect.run(task=nornir_netmiko.netmiko_send_command, command_string=comm)
    print_result(result)
