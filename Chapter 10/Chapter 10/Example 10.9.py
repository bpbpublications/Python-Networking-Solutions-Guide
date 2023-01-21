    def sftp_upload_to_servers(src_file, dest_file):
        with open("input/device_list.txt") as r:
            device_list = r.read().splitlines()
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        for ip in device_list:
            ssh.connect(hostname=ip, username="ubuntu", password="ubuntu")
            sftp = ssh.open_sftp()
            sftp.put(src_file,dest_file)
