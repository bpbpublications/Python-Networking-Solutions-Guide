from ftpretty import ftpretty

host = "10.10.10.1"
username = "admin"
password = "cisco"

def  upload(local_file, remote_file):
    ftp = ftpretty(host, username, password)
    ftp.put(local_file, remote_file)
    ftp.close()

def  download(local_file, remote_file):
    ftp = ftpretty(host, username, password)
    ftp.get(remote_file, local_file)
    ftp.close()


upload("test.txt","test.txt")
