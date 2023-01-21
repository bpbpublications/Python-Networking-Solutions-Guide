from paramiko import SSHClient, AutoAddPolicy

def sftp_connect():
    ssh = SSHClient()
    ssh.set_missing_host_key_policy (AutoAddPolicy())
    ssh.connect(hostname="192.168.163.137", username="ubuntu", password="ubuntu")
    sftp = ssh.open_sftp()
    return sftp

def sftp_upload(local_file,remote_file):
    sftp_connect().put(local_file,remote_file)
    sftp_connect().close()

def sftp_download(remote_file,local_file):
    sftp_d = sftp_connect()
    sftp_d.get(remote_file,local_file)
    sftp_d.close()

sftp_upload("test.txt","test.txt")
