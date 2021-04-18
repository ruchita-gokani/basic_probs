"""Given a hostname as input. print all the IP addresses of the host. Assume SSH keys are in place for root user.
# ./getIPaddress.py web1.facebook.com
# 127.0.0.1
# 10.3.3.4
# 192.168.0.12"""
import subprocess
import re
import sys


def getIPaddress(hostname):

    command = ["ssh", hostname, "ifconfig", "|", "grep", "inet"]
    r = subprocess.run(command, capture_output=True, text=True)
    # without using re: ifconfig -a | grep 'inet' | awk '{print $2}'
    pattern = re.compile(r'(?:inet)+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    # pattern = re.compile(r'(?:inet)+\s([0-9]{1,3}\.{3}[0-9]{1,3})')
    matches = pattern.finditer(str(r.stdout))
    for match in matches:
        print(match.group(0))

if __name__=='__main__':
    hname = str(sys.argv[1]),
    getIPaddress(hname)