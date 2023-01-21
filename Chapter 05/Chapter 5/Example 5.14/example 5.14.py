import napalm

host = {"hostname": "10.10.10.1", "username": "admin", "password": "cisco"}

driver = napalm.get_network_driver("ios")
connect = driver(**host)

connect.open()
output = connect.load_merge_candidate(filename="command_list.txt")

print(connect.compare_config())
connect.commit_config()   
connect.close()
