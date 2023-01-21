import paramiko

def sftp_connect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy (paramiko.AutoAddPolicy())
    ssh.connect(hostname="10.10.30.1", username="admin", password="huawei")
    sftp = ssh.open_sftp()
    return sftp

def sftp_upload(local_file,remote_file):
    sftp_connect().put(local_file,remote_file)
    sftp_connect().close()

def sftp_download(remote_file,local_file):
    sftp_d = sftp_connect()
    sftp_d.get(remote_file,local_file)
    sftp_d.close()

sftp_download("remote_test.txt","local_test.txt")
