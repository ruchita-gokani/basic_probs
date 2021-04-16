"""# Given a log file containing two days of web server logs,
# find the percentage of users who visited the site on
# both days. The log file contains the following
# columns, separated by spaces.

# Date, Operation, Path, User, Status Code
# 2019-02-02T18:83:03 GET /some/webpage.html ted 200
# 2019-02-02T18:83:03 GET /some/otherpage.html ted 200
# 2019-02-02T18:83:03 GET /some/otherwebpage.html sue 200
# 2019-02-02T18:83:03 GET /some/third.html josh 404
"""

from __future__ import division

with open('usage_files/web_views.log', 'r') as log_file:
	line1 = log_file.readline()
	log_content = log_file.read()
	line = log_content.split('\n')
	my_dict = {}
	for l in line:
		datetime = l.split(' ')[0]
		date = datetime.split('T')[0]
		user = l.split(' ')[3]
		try:
			my_dict[date].add(user)
		except KeyError:
			my_dict[date] = {user}
	values = [my_dict[key] for key in my_dict.keys()]
	common_users = len(set.intersection(*values))
	total_users = len(set.union(*values))
	percent_users = common_users/total_users*100
	print my_dict, values, percent_users
