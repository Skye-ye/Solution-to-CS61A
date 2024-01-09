from link import *

def filter_link(link, f):
	while link is not Link.empty:
		if f(link.first):
			yield link.first
		link = link.rest