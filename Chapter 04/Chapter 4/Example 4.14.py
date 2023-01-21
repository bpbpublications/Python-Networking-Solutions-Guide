enter_ip = input("\nEnter an IP address: ")
octet_list = []
ip = enter_ip.split(".")         #Divide ip address to octets by "." dot character

for octet in ip:                            #Check all octets are digits (not contain any non-digit character)
    try:
        octet_list.append(int(octet))       #Convert each item in list to integer, if fail, continue
    except:                          #So if fail,octet list will not be 4 anymore.
        continue                     #And below if condition will not be matched

if len(octet_list) == 4 and 0 < octet_list[0] < 255 and  0 <= octet_list[1] <= 255 and  0 <= octet_list[2] <= 255  and  0 <= octet_list[3] <= 255 :

    mask = input("\nEnter a Subnet Mask (1 to 32):  address: ")
    try:
        number = int(mask) # Convert input to integer, if fail, continue
        if  0 < number <= 32:
            # Find 0/8/16/24 main classes
            a = int(int(mask) / 8)

            # Find sub-class like 18,25,26, etc.
            b = int(mask) % 8
            octet1 = 2 ** 8 - 2 ** (8 - b)  # Find subclass value

            z = octet_list[a]       #Find  the octet to change
            k = int(z / 2 ** (8 - b))   #
            net = ((2 ** (8 - b)) * k)  #network address calculation
            brod = ((2 ** (8 - b)) * (k + 1)) - 1   #Broadcast address calculation
            min_host = net + 1      #Min avaliable host
            max_host = brod - 1     #Max avaliable host

            # Find subclass value
            if a == 0:
                subnet = "x.0.0.0"
                wildcard = "y.255.255.255"
                total_host = ((256-octet1)*(256**3))-2
                network = "{}.{}.{}.{}".format(net,0,0,1)
                broadcast = "{}.{}.{}.{}".format(brod,255,255,255)
                min_host = "{}.{}.{}.{}".format(net,0,0,2)
                max_host = "{}.{}.{}.{}".format(brod,255,255,254)

            elif a == 1:
                subnet = "255.x.0.0"
                wildcard = "0.y.255.255"
                total_host = ((256-octet1)*(256**2))-2
                network = "{}.{}.{}.{}".format(octet_list[0],net,0,1)
                broadcast = "{}.{}.{}.{}".format(octet_list[0],brod,255,255)
                min_host = "{}.{}.{}.{}".format(octet_list[0],net,0,2)
                max_host = "{}.{}.{}.{}".format(octet_list[0],brod,255,254)

            elif a == 2:
                subnet = "255.255.x.0"
                wildcard = "0.0.y.255"
                total_host = ((256-octet1)*256)-2
                network = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],net,1)
                broadcast = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],brod,255)
                min_host = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],net,2)
                max_host = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],brod,254)

            elif a == 3:
                subnet = "255.255.255.x"
                wildcard = "0.0.0.y"
                total_host = (256-octet1)-2
                network = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],octet_list[2],net)
                broadcast = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],octet_list[2],brod)
                min_host = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],octet_list[2],min_host)
                max_host = "{}.{}.{}.{}".format(octet_list[0],octet_list[1],octet_list[2],max_host)

            subnet_new = subnet.replace("x", str(octet1))  #Replace x value in subnet with octet1
            wildcard = wildcard.replace("y", str(255 - octet1))

            print("-------------\nIP Address: {}".format(enter_ip))
            print("Subnet Mask: {}".format(mask))
            print("Subnet: {}".format(subnet_new))
            print("Wildcard: {}".format(wildcard))
            print("Total Host: {}".format(total_host))
            print("Network Address: {}".format(network))
            print("Broadcast Address: {}".format(broadcast))
            print("IP Address Range: {} - {}".format(min_host,max_host) )

        else:
            print("ERROR: INVALID IP ADDRESS")
    except:             # So if fail,octet list will not be 4 anymore.
        print("ERROR: INVALID IP ADDRESS")

else:
    print("ERROR: INVALID IP ADDRESS")