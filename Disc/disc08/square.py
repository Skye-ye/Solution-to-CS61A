from tree import *

def square_tree(t):
	t.label = t.label ** 2
	for branch in t.branches:
		square_tree(branch)