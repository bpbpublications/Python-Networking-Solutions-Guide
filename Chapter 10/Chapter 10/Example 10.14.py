    def ping_test(ip,ping_count):
        output = ""	
        print(f"\n---Try to Ping: {ip} ---")
        data = Popen(f"cmd /c ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")
        for line in data.stdout:
            output = output + "\n" + line.rstrip('\n')
        print(output)
