enter_ip = input("\nEnter an IP address: ")

ip = enter_ip.split(".")
valid = 0

if len(ip) == 4:
    try:
        for x in ip:
            if 0 <= int(x) < 256:
                valid = valid + 1
            else:
                print("This is NOT a VALID IP Address")
                break
        if valid == 4:
            print(f"{enter_ip} is a VALID IP Address")
    except:
        print ("This is NOT a VALID IP Address")

else:
    print ("This is NOT a VALID IP Address")