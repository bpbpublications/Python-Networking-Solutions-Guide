from netmiko import Netmiko

ip_list = [ "10.10.10.1", "10.10.10.2", "10.10.10.3", "10.10.20.1", "10.10.30.1" ]
device_list = ["cisco_ios","cisco_ios","cisco_ios","juniper_junos","huawei"]

for ip,device in zip(ip_list,device_list):

    ip = {
        "host": f"{ip}",
        "username":"admin",
        "password":"cisco",
        "device_type": f"{device}",
        "global_delay_factor": 0.1
    }

    if ip["device_type"] == "cisco_ios":
        command = "show run"
    elif ip["device_type"] == "juniper_junos":
        command = "show configuration | display set"
    elif ip["device_type"] == "huawei":
        command = "display current-configuration"
    else:
        print("This is different vendor (Not Cisco,Huawei or Juniper)")

    try:
        print(f"\n----Try to login: {ip['host']}---\n")
        net_connect = Netmiko(**ip)
        output = net_connect.send_command(command)

    except:
        print(f"***Cannot login to {ip['host']}")


    with open (f"{ip['host']}.txt","w") as w:
        w.write(output)
