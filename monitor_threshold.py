'''
# I want to monitor a value produced from a streaming app; say one of the swap columns from vmstat. If the value exceeds a given threshold X for more than Y consecutive samples I'd like a message printed out.
#
# The command should take standard input and be invoked as:
#
# yourscript <column_number> <repetitions> <threshold value>
#
# Example: vmstat 1 | yourscript 7 5 200
#
# That means that when the value of column 7 has gone over 200 for more than 5 times in a row, print something out. My plan is to leave this running over night and check back on it in the morning.
# Output -
# 5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
# 5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
# 5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
# 5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
# 5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
# 5 4 0 556532 1698688 32809712 201 0 0 1304 3168 6853 31 1 58 11 0
# 5 4 0 517944 1698696 32809792 0 0 0 1360 3345 10589 31 1 53 15 0
# 6 4 0 477476 1698748 32836968 300 0 4 1459 3819 20150 39 2 42 17 0
'''

def thresh_monitor(column_number, repetitions, threshold):
	with open('vm_stat.log', 'r') as vm_stat:
		log_file = vm_stat.read()
		lines = log_file.split('\n')
		count  = 0
		for l in lines:
			line_value = l.split(' ')
			if int(line_value[column_number-1]) >= threshold:
				count +=1
				if count == repetitions:
					return "Alert!"
			else: 
				count=0
			
			
			
print thresh_monitor(12, 5, 6854)
