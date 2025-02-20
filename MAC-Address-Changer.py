import subprocess

def change_mac_address(interface, new_mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    print(f"MAC address changed to {new_mac_address} on interface {interface}")

# Example usage
interface = "eth0"  # Replace with the desired interface
new_mac_address = "00:11:22:33:11:11"  # Replace with the desired new MAC address

change_mac_address(interface, new_mac_address)
