from netmiko import Netmiko

ip_list = [ "10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.10.4" ]

for ip in ip_list:
    ip = {
        "host": f"{ip}",
        "username":"admin",
        "password":"cisco",
        "device_type": "cisco_ios",
        "global_delay_factor": 0.1
    }

    try:
        print(f"\n---Try to Login: {ip['host']} ---\n")
        net_connect = Netmiko(**ip)
        output = net_connect.send_command("show interface description")
        print(output)
    except:
        print(f"***Cannot login to {ip['host']}")
