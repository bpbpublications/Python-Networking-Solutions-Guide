from re import findall
from subprocess import Popen, PIPE
from matplotlib import pyplot as plt
from netmiko import Netmiko
from time import sleep
from datetime import datetime


class tools:
    def subnet_calculator(ip_address,subnet_mask):
        octet_list = []
        ip = ip_address.split(".")  # Divide ip address to octets by "." dot character

        for octet in ip:  # Check all octets are digits (not contain any non-digit character)
            try:
                octet_list.append(int(octet))  # Convert each item in list to integer, if fail, continue
            except:  # So if fail,octet list will not be 4 anymore.
                continue  # And below if condition will not be matched

        if len(octet_list) == 4 and 0 < octet_list[0] < 255 and 0 <= octet_list[1] <= 255 and 0 <= octet_list[
            2] <= 255 and 0 <= octet_list[3] <= 255:

            try:
                number = int(subnet_mask)  # Convert input to integer, if fail, continue
                if 0 < number <= 32:
                    # Find 0/8/16/24 main classes
                    a = int(int(subnet_mask) / 8)

                    # Find sub-class like 18,25,26, etc.
                    b = int(subnet_mask) % 8
                    octet1 = 2 ** 8 - 2 ** (8 - b)  # Find subclass value

                    z = octet_list[a]  # Find  the octet to change
                    k = int(z / 2 ** (8 - b))
                    net = ((2 ** (8 - b)) * k)  # network address calculation
                    brod = ((2 ** (8 - b)) * (k + 1)) - 1  # Broadcast address calculation
                    min_host = net + 1  # Min avaliable host
                    max_host = brod - 1  # Max avaliable host

                    # Find subclass value
                    if a == 0:
                        subnet = "x.0.0.0"
                        wildcard = "y.255.255.255"
                        total_host = ((256 - octet1) * (256 ** 3)) - 2
                        network = "{}.{}.{}.{}".format(net, 0, 0, 1)
                        broadcast = "{}.{}.{}.{}".format(brod, 255, 255, 255)
                        min_host = "{}.{}.{}.{}".format(net, 0, 0, 2)
                        max_host = "{}.{}.{}.{}".format(brod, 255, 255, 254)

                    elif a == 1:
                        subnet = "255.x.0.0"
                        wildcard = "0.y.255.255"
                        total_host = ((256 - octet1) * (256 ** 2)) - 2
                        network = "{}.{}.{}.{}".format(octet_list[0], net, 0, 1)
                        broadcast = "{}.{}.{}.{}".format(octet_list[0], brod, 255, 255)
                        min_host = "{}.{}.{}.{}".format(octet_list[0], net, 0, 2)
                        max_host = "{}.{}.{}.{}".format(octet_list[0], brod, 255, 254)

                    elif a == 2:
                        subnet = "255.255.x.0"
                        wildcard = "0.0.y.255"
                        total_host = ((256 - octet1) * 256) - 2
                        network = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], net, 1)
                        broadcast = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], brod, 255)
                        min_host = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], net, 2)
                        max_host = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], brod, 254)

                    elif a == 3:
                        subnet = "255.255.255.x"
                        wildcard = "0.0.0.y"
                        total_host = (256 - octet1) - 2
                        network = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], octet_list[2], net)
                        broadcast = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], octet_list[2], brod)
                        min_host = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], octet_list[2], min_host)
                        max_host = "{}.{}.{}.{}".format(octet_list[0], octet_list[1], octet_list[2], max_host)

                    subnet_new = subnet.replace("x", str(octet1))  # Replace x value in subnet with octet1
                    wildcard = wildcard.replace("y", str(255 - octet1))

                    print("-------------\nIP Address: {}".format(ip_address))
                    print("Subnet Mask: {}".format(subnet_mask))
                    print("Subnet: {}".format(subnet_new))
                    print("Wildcard: {}".format(wildcard))
                    print("Total Host: {}".format(total_host))
                    print("Network Address: {}".format(network))
                    print("Broadcast Address: {}".format(broadcast))
                    print("IP Address Range: {} - {}".format(min_host, max_host))

                else:
                    print("ERROR: INVALID IP ADDRESS")
            except:  # So if fail,octet list will not be 4 anymore.
                print("ERROR: INVALID IP ADDRESS")

        else:
            print("ERROR: INVALID IP ADDRESS")



    def ping_test(ip,ping_count):
        output = ""
        print(f"\n---Try to Ping: {ip} ---")
        data = Popen(f"cmd /c ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")
        for line in data.stdout:
            output = output + "\n" + line.rstrip('\n')
        print(output)



class plotting:
    def cpu_plot(ip):
        host = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
        count = 7
        delay = 3
        command = "show processes cpu"
        cpu_levels = []
        time_list = []
        net_connect = Netmiko(**host)

        for i in range(1, count):
            print(f"Get CPU levels count: {i}")
            output = net_connect.send_command(command)
            time = datetime.now().strftime("%H:%M:%S")
            time_list.append(time)
            sleep(delay)

            cpu_data = findall("CPU utilization for five seconds: (\d+)%/", output)
            cpu_levels.append(int(cpu_data[0]))
            print("CPU Level: ", cpu_data[0])

        plt.plot(time_list, cpu_levels)
        plt.xlabel("Time")
        plt.ylabel("CPU Levels in %")
        plt.grid(True)
        plt.show()



    def interface_bandwidth_plot(ip, interface):
        host = {"host": ip, "username": "admin", "password": "cisco", "device_type": "cisco_ios"}
        count = 5
        delay = 3
        inbound_rate = []
        outbound_rate = []
        time_list = []
        net_connect = Netmiko(**host)

        for i in range(1, count):
            output = net_connect.send_command(f"show interfaces {interface}")
            time = datetime.now().strftime("%H:%M:%S")
            time_list.append(time)

            input_level = findall("5 minute input rate (\d+)", output)
            output_level = findall("5 minute output rate (\d+)", output)
            inbound_rate.append(int(input_level[0]))
            outbound_rate.append(int(output_level[0]))
            sleep(delay)

            print("Input Level: ", input_level[0])
            print("Output Level: ", output_level[0])

        plt.plot(time_list, inbound_rate, color="blue", label="Inbound")
        plt.plot(time_list, outbound_rate, color="red", label="Outbound")
        plt.xlabel("Time")
        plt.ylabel("Interface Levels in MBs")
        plt.title(f"Interface Rate of {host['host']} - {interface}")
        plt.show()