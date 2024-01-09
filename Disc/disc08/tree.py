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
