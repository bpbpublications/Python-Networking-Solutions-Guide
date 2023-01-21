class transfer_files:
    def scp_upload_to_routers(src_file, dest_file):
        if not dest_file:
            dest_file = src_file
        connect = InitNornir(config_file="hosts.yaml")
        result = connect.run(task=netmiko_file_transfer, source_file=src_file, dest_file=dest_file, direction="put")
        print_result(result)
