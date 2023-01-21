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
