from ftpretty import ftpretty

host = "10.10.30.1"
username = "admin"
password = "huawei"

ftp = ftpretty(host, username, password)

a=ftp.list(extra=True)
for i in range(len(a)):
print("File:",a[i]["name"], "- Size:", a[i]["size"], "Bytes")
