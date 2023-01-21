command_change = [
"""interface GigabitEthernet0/0
 description TEST""",

"interface GigabitEthernet0/0",

"""interface GigabitEthernet0/1
 no ip address
 shutdown""",

"""interface GigabitEthernet0/1
 ip address 192.168.10.10 255.255.255.0"""
]

item_count = len(command_change)

with open("old_config.txt") as old_config:
    new_config = old_config.read()

for x in range(0, item_count, 2):
    new_config = new_config.replace(command_change[x], command_change[x + 1])

with open("new_config.txt", "w") as new:
    new.write(new_config)
