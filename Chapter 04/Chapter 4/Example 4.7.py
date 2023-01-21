import telnetlib

host = ["10.10.10.1","10.10.10.2","10.10.10.3"]
user = "admin"
password = "cisco"
command = ["terminal length 0","show ip interface brief","show clock","exit"]

for ip in host:
    tel = telnetlib.Telnet(ip, 23, timeout=1)
    tel.read_until(b"Username:")
    tel.write(user.encode('ascii') + b"\n")
    tel.read_until(b"Password:")
    tel.write(password.encode('ascii') + b"\n")

    for config in command:
        tel.write(config.encode("ascii") + b"\n")
        print(tel.read_all().decode('ascii'))