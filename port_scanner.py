#!/bin/python3
import pyfiglet
import sys
import socket
from datetime import datetime

try:
    target = sys.argv[1]

except IndexError:
    print("Syntax Error  - python3 port_scanner.py <target_ip>")
    sys.exit(1)

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


#Banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)


try:
    #Scan every port on the target IP
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

    #Return open port
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[*]Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting: (")
    sys.exit(0)

except socket.error:
    print("\nHost not responding :(")
    sys.exit(1)


