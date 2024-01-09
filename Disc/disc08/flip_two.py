from link import *

def flip_two(lnk):
	def flip_helper(l, depth=0):
		if l is not Link.empty and l.rest is not Link.empty:
			if depth % 2 == 0:
				l.first, l.rest.first = l.rest.first, l.first
			depth+=1
			flip_helper(l.rest, depth)
	return flip_helper(lnk)