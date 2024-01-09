def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def fib_tree(n):
	if n <= 1:
		return tree(n)
	else:
		left, right = fib_tree(n - 2), fib_tree(n - 1)
		return tree(label(left) + label(right), [left, right])

def count_leaves(tree):
	if is_leaf(tree):
		return 1
	else:
		return sum([count_leaves(branch) for branch in branches(tree)])

def leaves(tree):
	if is_leaf(tree):
		return [label(tree)]
	else:
		return sum([leaves(branch) for branch in branches(tree)], [])

def increment_leaves(t):
	if is_leaf(t):
		return tree(label(t) + 1)
	else:
		bs = [increment_leaves(branch) for branch in branches(t)]
		return tree(label(t), bs)

def increment(t):
	return tree(label(t) + 1, [increment(branch) for branch in branches(t)])

def print_tree(t, indent=0):
	print('  ' * indent + str(label(t)))
	for branch in branches(t):
		print_tree(branch, indent+1)

def height(t):
	if is_leaf(t):
		return 0
	else:
		return 1 + max([height(branch) for branch in branches(t)])

def max_path_sum(t):
	if is_leaf(t):
		return label(t)
	else:
		return label(t) + max([max_path_sum(branch) for branch in branches(t)])

def square_tree(t):
	if is_leaf(t):
		return tree(label(t) ** 2)
	else:
		return tree(label(t) ** 2, [square_tree(branch) for branch in branches(t)])

def find_path(tree, x):
	if label(tree) == x:
		return [x]

	for branch in branches(tree):
		path = find_path(branch, x)
		if path:
			return [label(tree)] + path

	return None

def find_all_path(tree, x):
	paths = []

	if label(tree) == x:
		paths.append([x])

	for branch in branches(tree):
		for path in find_all_path(branch, x):
			paths.append([label(tree)] + path)

	return paths

def prune_binary(t, nums):
	if is_leaf(t):
		if label(t) in nums:
			return t
		return None
	else:
		next_valid_nums = [num[1:] for num in nums if num.startswith(label(t))]
		new_branches = []
		for branch in branches(t):
			pruned_branch = prune_binary(branch, next_valid_nums)
			if pruned_branch is not None:
				new_branches = new_branches + [pruned_branch]
		if not new_branches:
			return None
		return tree(label(t), new_branches)

















