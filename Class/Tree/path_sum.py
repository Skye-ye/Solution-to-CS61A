from tree import *

haste = tree('h', [tree('a', [tree('s'), tree('t')]), tree('e')])

def print_sums(t, path_sum):
	path_sum = path_sum + label(t)
	if is_leaf(t):
		print(path_sum)
	else:
		for branch in branches(t):
			print_sums(branch, path_sum)
