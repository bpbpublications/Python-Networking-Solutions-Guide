import napalm
import json

host = {"hostname": "10.10.10.1", "username": "admin", "password": "cisco"}

driver = napalm.get_network_driver("ios")
connect = driver(**host)

connect.open()
output = connect.get_interfaces()

print(json.dumps(output, indent=1))
connect.close()