    def config_with_nornir():
        with open("input/command_list.txt") as r:
            command_list = r.read().splitlines()
        connect = InitNornir(config_file="hosts.yaml")
        result = connect.run(task=netmiko_send_config, config_commands=command_list)
        print_result(result)
