from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, s, e):
        IPv4Network.__init__(self, (s, e), strict=False)

    def regular(self):
        return not (self.is_multicast |
                    self.is_loopback |
                    self.is_private |
                    self.is_reserved |
                    self.is_unspecified)

randnet = random.randint(0x0B0000000, 0xDF000000)
randmask = random.randint(8, 24)

net = IPv4RandomNetwork(randnet, randmask)
net2 = sorted(net)

print(net2, net.regular())

