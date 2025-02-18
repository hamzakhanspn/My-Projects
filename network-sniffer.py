from scapy.all import *

def scan_network(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    return [(received.psrc, received.hwsrc) for sent, received in result]

network = "192.168.29.1/24"
scan_results = scan_network(network)
print("IP" + " "*18+"MAC")
for result in scan_results:
    print(f"{result[0]:16} {result[1]}")
