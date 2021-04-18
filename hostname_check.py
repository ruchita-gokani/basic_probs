"""# Given a range of hostnames, print a list of hosts running the wrong number of instances of a process.
# Don't worry about authentication, assume ssh keys are in place for user 'root'.
#
# Hostname range: web0001-1000.facebook.com
# Process name: "app"
# Number of running "app" instances when healthy: 4
#
# Example invocation: ./appcheck web0001-1000.facebook.com app 4
"""

import sys
import subprocess
import re


def check_process_count(host_range, process, lim):
    pattern = re.compile(r'([a-zA-Z.]+)([0-9-]+)([a-zA-Z.]+)')
    matches = pattern.finditer(host_range)
    num, hname, dname = '', '', ''
    for match in matches:
        num = match.group(2)
        hname = match.group(1)
        dname = match.group(3)
    n = num.split('-')
    ns, nl = int(n[0]), int(n[1])
    res = []
    for i in range(ns,nl+1):
        fqdn = hname+str(i)+dname
        command = ["ssh", fqdn, "ps -ef", "|", "pgrep", process, "|", "wc -l"]
        p1 = subprocess.run(command, capture_output=True, text=True)
        if int(p1.stdout) != lim:
            res.append(fqdn)
    return res


if __name__ == '__main__':
    hostname, proc, limit = sys.argv[1], sys.argv[2], int(sys.argv[3])
    print(check_process_count(hostname, proc, limit))

