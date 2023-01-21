import telnetlib

ip = "10.10.10.1"
user = "admin"
password = "cisco"

tel = telnetlib.Telnet(ip, 23, timeout=1)
tel.read_until(b"Username:")
tel.write(user.encode('ascii') + b"\n")
tel.read_until(b"Password:")
tel.write(password.encode('ascii') + b"\n")

tel.write(b"show ip interface brief\n")
tel.write(b"exit\n")

print(tel.read_all().decode('ascii'))