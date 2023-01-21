from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

connect = InitNornir(config_file="config.yaml")

result = connect.run(task=netmiko_send_command, command_string="show arp")

print_result(result)
