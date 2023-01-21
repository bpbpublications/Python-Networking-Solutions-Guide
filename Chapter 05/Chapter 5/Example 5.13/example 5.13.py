import napalm
import json

ip_list = ["10.10.10.1","10.10.10.2","10.10.10.3"]

for ip in ip_list:
    print(f"*** Connecting to {ip} ***")
    host = {"hostname": ip, "username": "admin", "password": "cisco"}

    driver = napalm.get_network_driver("ios")
    connect = driver(**host)

    connect.open()
    output = connect.get_arp_table()
    print(json.dumps(output, indent=1))
    connect.close()
