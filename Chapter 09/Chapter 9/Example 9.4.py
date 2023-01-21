from scapy.all import *

ip_address = IP(dst="8.8.8.8")
icmp_sequence= ICMP(seq=1111)

pckt= ip_address / icmp_sequence

send(pckt)
