import ftplib
import re
import os

host = "10.10.30.1"
username = "admin"
password = "huawei"
filename = "test.txt"
files = []
ftp = ftplib.FTP(host, username, password)
output = ftp.dir(files.append)
files = " ".join(files)

file_size = re.findall(f"(\d+)\s+\w+\s+\d+\s+\d+:\d+\s+{filename}", files)
local = os.path.getsize(filename)
if int(local) == int(file_size[0]):
    print(f"'{filename}': '{local}' Bytes. It's same on local and remote host.")
else:
    print("ERROR: File size has problem.")
