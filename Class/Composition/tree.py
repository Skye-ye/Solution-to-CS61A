class Tree:
	"""A tree is a label and a list of branches."""
	def __init__(self, label, branches=[]):
		self.label = label
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)

	def __repr__(self):
		if self.branches:
			branch_str = ', ' + repr(self.branches)
		else:
			branch_str = ''
		return 'Tree({0}{1})'.format(repr(self.label), branch_str)

	def __str__(self):
		return '\n'.join(self.indented())

	def indented(self):
		lines = []
		for b in self.branches:
			for line in b.indented():
				lines.append('  ' + line)
		return [str(self.label)] + lines

	def is_leaf(self):
		return not self.branches


def fib_tree(n):
	"""A Fibonacci tree.

	>>> print(fib_tree(4))
	3
	  1
		0
		1
	  2
		1
		1
		  0
		  1
	"""
	if n == 0 or n == 1:
		return Tree(n)
	else:
		left = fib_tree(n-2)
		right = fib_tree(n-1)
		fib_n = left.label + right.label
		return Tree(fib_n, [left, right])


def leaves(tree):
	"""Return the leaf values of a tree.

	>>> leaves(fib_tree(4))
	[0, 1, 1, 0, 1]
	"""
	if tree.is_leaf():
		return [tree.label]
	else:
		return sum([leaves(b) for b in tree.branches], [])


def height(tree):
	"""The height of a tree."""
	if tree.is_leaf():
		return 0
	else:
		return 1 + max([height(b) for b in tree.branches])


def prune(t, n):
	"""Prune sub-trees whose label value is n.

	>>> t = fib_tree(5)
	>>> prune(t, 1)
	>>> print(t)
	5
	  2
	  3
		2
	"""
	t.branches = [b for b in t.branches if b.label != n]
	for b in t.branches:
		prune(b, n)