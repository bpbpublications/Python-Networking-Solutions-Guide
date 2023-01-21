from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

commands = ["snmp-server community public RO", "snmp-server community private RW",
            "snmp-server enable traps cpu threshold", 
            "snmp-server host 10.10.10.150 version 2c snmp_user", 
            "snmp-server source-interface informs GigabitEthernet0/0"]

connect = InitNornir()

result = connect.run(task=netmiko_send_config, config_commands=commands)
print_result(result)
