"""
I want to monitor a value produced from a streaming app; say one of the swap columns from vmstat.
If the value exceeds a given threshold X for more than Y consecutive samples I'd like a message printed out.

The command should take standard input and be invoked as:

yourscript <column_number> <repetitions> <threshold value>

Example: vmstat 1 | yourscript 7 5 200

That means that when the value of column 7 has gone over 200 for more than 5 times in a row, print something out. My plan is to leave this running over night and check back on it in the morning.
Output -
5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
5 4 0 517944 1698696 32809792 0 0 0 1360 3345 10589 31 1 53 15 0
6 4 0 477476 1698748 32836968 300 0 4 1459 3819 20150 39 2 42 17 0
"""

import sys


def thresh_monitor(column_number, repetitions, threshold):
	exceeds_message = "The recommended threshold has been exceeded"
	passing_message = "The numbers are within the limits of threshold"
	with open('vm_stat.log', 'r') as vm_stat:
		log_file = vm_stat.read()
		lines = log_file.split('\n')
		count = 0
		for line in lines:
			line_value = line.split(' ')
			column = column_number - 1
			if int(line_value[column]) >= threshold:
				count +=1
				if count == repetitions:
					break
			else:
				count = 0
		if count >= repetitions:
			return exceeds_message
		else:
			return passing_message


def main():
	"""Get arguments and pass them to thresh_monitor function"""
	if len(sys.argv) > 3:
		s1, s2, s3 = sys.argv[1], sys.argv[2], sys.argv[3]
	else:
		s1 = input('Enter column_number: ')
		s2 = input('Enter repetitions: ')
		s3 = input('Enter threshold: ')
	column_number, repetitions, threshold = int(s1), int(s2), int(s3)
	print(thresh_monitor(column_number, repetitions, threshold))

main()