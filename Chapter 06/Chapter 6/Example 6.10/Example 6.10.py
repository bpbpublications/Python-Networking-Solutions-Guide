from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_file_transfer

connect = InitNornir()

result = connect.run(task=netmiko_file_transfer, 
                     source_file="test.txt", 
                     dest_file="test.txt"
                     )

print_result(result)
