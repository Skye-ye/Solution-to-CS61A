from link import *

def sum_nums(lnk):
	total = 0
	while lnk is not Link.empty:
		total += lnk.first
		lnk = lnk.rest
	return total