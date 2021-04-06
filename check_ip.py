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