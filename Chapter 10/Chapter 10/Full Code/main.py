from InquirerPy import inquirer
from network_devices import *
from servers import *
from others import *

main_task = inquirer.select(
    message="Choose a Main Task:",
    choices=["Collect Logs", "Device Configuration", "File Transfer", "Server Configuration", "Others", "Exit"]).execute()




if main_task == "Collect Logs":
    sub_task = inquirer.select(
        message="Choose a Sub Task:",
        choices=["From 1 Device", "From Multiple Devices", "Collect Device Information",
                 "Collect CPU Usage", "Send Collected Logs by Email", "Exit"]).execute()

    if sub_task == "From 1 Device":
        ip = inquirer.text(message="IP Address: ").execute()
        username = inquirer.text(message="Username: ").execute()
        password = inquirer.secret(message="Password: ").execute()
        command = inquirer.text(message="Command: ").execute()
        collect_logs.from_one_device(ip, username, password, command)

    elif sub_task == "From Multiple Devices":
        collect_logs.from_multiple_devices()

    elif sub_task == "Collect Device Information":
        collect_logs.collect_device_info()

    elif sub_task == "Collect CPU Usage":
        collect_logs.collect_cpu_usage()

    elif sub_task == "Send Collected Logs by Email":
        collect_logs.send_logs_by_email()

    elif sub_task == "Exit":
        print("Exited from the tool.")




elif main_task == "Device Configuration":
    sub_task = inquirer.select(
        message="Choose a Sub Task:",
        choices=["Configure With Netmiko", "Configure With Nornir", "Exit"]).execute()

    if sub_task == "Configure With Netmiko":
        result = inquirer.confirm(message="\n**IP addresses in 'input/device_list.txt'\n**Commands in 'input/command_list.txt'\n").execute()
        if result:
            configure_device.config_with_netmiko()
        else:
            print("Exited from the tool.")

    elif sub_task == "Configure With Nornir":
        result = inquirer.confirm(message="\n**IP addresses in 'hosts.yaml'\n**Commands in 'input/command_list.txt'\n").execute()
        if result:
            configure_device.config_with_nornir()
        else:
            print("Exited from the tool.")

    elif sub_task == "Exit":
        print("Exited from the tool.")




elif main_task == "File Transfer":
    sub_task = inquirer.select(
        message="Choose a Sub Task:",
        choices=["Upload with SCP to Routers", "Upload with SFTP to Servers", "Exit"]).execute()

    if sub_task == "Upload with SCP to Routers":
        src_file = inquirer.text(message="Source File on PC: ").execute()
        dest_file = inquirer.text(message="Destination File: ").execute()
        transfer_files.scp_upload_to_routers(src_file, dest_file)

    elif sub_task == "Upload with SFTP to Servers":
        src_file = inquirer.text(message="Source File on PC: ").execute()
        dest_file = inquirer.text(message="Destination File: ").execute()
        transfer_files.sftp_upload_to_servers(src_file, dest_file)

    elif sub_task == "Exit":
        print("Exited from the tool.")




elif main_task == "Server Configuration":
    sub_task = inquirer.select(
        message="Choose a Sub Task:",
        choices=["Configure or Collect Info", "Collect Resource Usage",
                 "Collect Interface Information ", "Install Packages", "Exit"]).execute()

    if sub_task == "Configure or Collect Info":
        result = inquirer.confirm(message="\n**IP addresses in 'input/device_list.txt'\n**Commands in 'input/command_list.txt'\n").execute()
        if result:
            config_and_collect_logs.config_collect_logs()
        else:
            print("Exited from the tool.")

    elif sub_task == "Collect Resource Usage":
        config_and_collect_logs.collect_resource_usage()

    elif sub_task == "Collect Interface Information ":
        config_and_collect_logs.collect_interface_information()

    elif sub_task == "Install Packages":
        package_name = inquirer.text(message="Enter Package Name: ").execute()
        result = inquirer.confirm(message="\n**IP addresses in 'input/device_list.txt'\n").execute()
        if result:
            config_and_collect_logs.package_installation(package_name)
        else:
            print("Exited from the tool.")

    elif sub_task == "Exit":
        print("Exited from the tool.")




elif main_task == "Others":
    sub_task = inquirer.select(
        message="Choose a Sub Task:",
        choices=["Subnet Calculator", "Ping Test", "Plotting CPU Levels", "Plotting Interface Bandwidth", "Exit"]).execute()

    if sub_task == "Subnet Calculator":
        ip_address = inquirer.text(message="Enter an IP address: ").execute()
        subnet_mask = inquirer.text(message="Enter a Subnet Mask (1 to 32): ").execute()
        tools.subnet_calculator(ip_address, subnet_mask)

    elif sub_task == "Ping Test":
        ip_address = inquirer.text(message="Enter an IP address: ").execute()
        ping_count = inquirer.text(message="Enter Quantity of Ping Packets: ").execute()
        tools.ping_test(ip_address, ping_count)

    elif sub_task == "Plotting CPU Levels":
        ip_address = inquirer.text(message="Enter an IP address: ").execute()
        plotting.cpu_plot(ip_address)

    elif sub_task == "Plotting Interface Bandwidth":
        ip_address = inquirer.text(message="Enter an IP address: ").execute()
        interface_name = inquirer.text(message="Enter the Interface Name: ").execute()
        plotting.interface_bandwidth_plot(ip_address, interface_name)

    elif sub_task == "Exit":
        print("Exited from the tool.")




elif main_task == "Exit":
    print("Exited from the tool.")