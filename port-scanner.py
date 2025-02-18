from scapy.all import *

def scan_ports(target_ip, ports):
    print(f"Scanning ports on {target_ip}...")
    for port in ports:
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response is None:
            print(f"Port {port} is filtered or closed")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

def main():
    target_ip = "192.168.29.1"
    ports = [20, 21, 22, 23, 25, 50, 80, 123, 139, 443, 449, 554, 3306, 3389, 4444, 5037, 5800, 5900]
    scan_ports(target_ip, ports)

if __name__ == "__main__":
    main()
