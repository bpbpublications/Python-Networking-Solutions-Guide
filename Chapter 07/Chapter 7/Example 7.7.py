from re import findall
from pandas import DataFrame
from subprocess import Popen, PIPE

host = ["10.10.10.1","123.214.2.3","www.google.com", "192.168.123.24", "8.8.8.8"]
ping_count = "3"
packet_loss, ip_list, status_list, sent_list, received_list, lost_list = ([] for i in range(6))


for ip in host:
    data = ""
    print(f"\n---Try to Ping: {ip} ---")
    output= Popen(f"cmd /c ping {ip} -n {ping_count}",stdout=PIPE,encoding="utf-8")
    for line in output.stdout:
        data = data +"\n" + line.rstrip('\n')
    print(data)
    ping_test = findall("TTL", data) #Check TTL word if the ping is successful or not
    if ping_test:
        status = "Successful"  #Ping Successful or Failed
        sent = findall("Sent = (\d+)", data)  #Find Sent packet number
        received = findall("Received = (\d+)", data)  #Find received packet number
        lost = findall("Lost = (\d+)", data)  #Find lost packets number
        loss = findall("\((.*) loss", data)  #Get loss packet percentage

    else:
        status = "Failed"
        sent = findall("Sent = (\d+)", data)
        received = ["0"]
        lost = sent
        loss = ["100%"]

    sent_list.append(sent[0])
    received_list.append(received[0])
    lost_list.append(lost[0])
    packet_loss.append(loss[0])
    ip_list.append(ip)
    status_list.append(status)

    df = DataFrame({"IP Address": ip_list, "Status": status_list, "Sent": sent_list, "Received": received_list, "Lost": lost_list, "Packet Loss Rate": packet_loss})
    df.to_excel("Ping Result.xlsx", sheet_name="Ping", index=False)
