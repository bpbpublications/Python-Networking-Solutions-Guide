import ftplib	

host = "10.10.30.1"
username = "admin"
password = "huawei"
filename = "test.txt"  #Local PC Filename

ftp = ftplib.FTP(host,username,password)

with open(filename, "rb") as upload:
    ftp.storbinary(f"STOR {filename}", upload)

ftp.quit()
