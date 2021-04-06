"""Validate IP Address
Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.
For example, "	", "0.23.25.0", and "255.255.255.255" are valid IP addresses, while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.
Examples:
ip = '192.168.0.1' output: true ip = '0.0.0.0' output: true ip = '123.24.59.99' output: true ip = '192.168.123.456' output: false
Constraints:
[time limit] 5000ms
[input] string ip
[output] boolean"""

def check_ip(ip_address):
	split_values = ip_address.split('.')
	if len(split_values) != 4:
		return False
	else:
		for i in split_values:
			if len(i)>=2 and int(i[0]) == 0:
				return False
			elif 0 <= int(i) <= 255:
				continue
			else:
				return False
		return True
	

print check_ip("0.168.123.45")