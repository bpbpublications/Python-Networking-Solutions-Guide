from netmiko import Netmiko
from re import findall
from pandas import DataFrame

host = ["10.10.20.1", "10.10.20.2", "10.10.20.3"]
time_list, severity_list, description_list, ip_list = ([] for x in range(4))
total_minor = total_major = total_critical = 0

for ip in host:
    device = {f"host": {ip}, "username": "admin", "password": "juniper", "device_type": "juniper", "global_delay_factor": 0.1 }
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show system alarms")

    alarm_count = findall("(\d+) alarms currently active",output)
    alarms = split("\n",output)
    del alarms[0:4]
    total_alarms = total_alarms + len(alarms)
    minor_alarms = findall("Minor",output)
    major_alarms = findall("Major",output)
    critical_alarms = findall("Critical",output)

    total_minor = total_minor + len(minor_alarms)
    total_major = total_major + len(major_alarms)
    total_critical = total_critical + len(critical_alarms)

    for alarm_item in alarms:
        time = findall("\d+-\d+\d+ \d+:\d+:\d+ UTC", alarm_item)
        severity = findall("Minor|Major|Critical", alarm_item)
        description = findall("\d+-\d+\d+ \d+:\d+:\d+ UTC\s+\w+\s+(.*)", alarm_item)
        ip_list.append(f"{ip}")
        time_list.append(time[0])
        severity_list.append(severity[0])
        description_list.append(description[0])

        with pandas.ExcelWriter('Alarm List.xlsx') as writer:
            df1 = pandas.DataFrame({"Alarm Count": [total_alarms],"Minor": [total_minor],"Major": [total_major],"Critical": [total_critical]})
            df2 = pandas.DataFrame({"Device IP": ip_list, "Time": time_list, "Severity": severity_list, "Description": description_list})
            df1.to_excel(writer, sheet_name="Summary", index=False)
            df2.to_excel(writer, sheet_name="Alarms", index=False)
