from link import *

def multiply_lnks(lst_of_lnks):
	if any(lnk is Link.empty for lnk in lst_of_lnks):
		return Link.empty

	product = 1
	for lnk in lst_of_lnks:
		product *= lnk.first

	return Link(product, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))