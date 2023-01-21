import pyshark

capture = pyshark.LiveCapture(interface='Wi-Fi')
packets = capture.sniff_continuously(packet_count=3)

for pckt in packets:
    print (f"\n\nPacket: \n{pckt}")
