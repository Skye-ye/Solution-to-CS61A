from tree import *

def find_paths(t, entry):
	paths = []

	if t.label == entry:
		paths.append([entry])

	for branch in t.branches:
		for path in find_paths(branch, entry):
			paths.append([t.label] + path)

	return paths