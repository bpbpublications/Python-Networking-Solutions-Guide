from scapy.all import *

arp = ARP(pdst="192.168.1.1/24")
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
broadcast = ether / arp
hosts = srp(broadcast, timeout=1)[0]

for device in hosts:
    print(f"IP: {device[1].psrc}    MAC: {device[1].hwsrc}")
