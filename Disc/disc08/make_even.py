from tree import *

def make_even(t):
	if t.label % 2 == 1:
		t.label += 1
	for branch in t.branches:
		make_even(branch)