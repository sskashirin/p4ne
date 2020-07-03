import glob

ips = set()

for file_name in glob.glob("/Users/ss.kashirin/PycharmProjects/p4ne/Lab1.5/*.txt"):
    with open(file_name) as file:
        for line in file:
            if line.find("ip address") == 1 and ("dhcp") not in line:
                ips.add(line.replace("ip address", "").strip())

for i in ips:
    print(i)